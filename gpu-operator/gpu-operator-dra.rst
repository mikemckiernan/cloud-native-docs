.. license-header
  SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
  SPDX-License-Identifier: Apache-2.0

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

.. headings (h1/h2/h3/h4/h5) are # * = -

.. _gpu-operator-dra:

###########################################
Deploying the GPU Operator with DRA Support
###########################################

Starting with GPU Operator ${version}, you can deploy and manage the
`DRA Driver for NVIDIA GPUs <https://dra-driver-nvidia-gpu.sigs.k8s.io/docs/>`__ as a GPU Operator operand.
Configure the operand through ``ClusterPolicy.spec.draDriver`` or the equivalent ``draDriver.*`` Helm values.

The integration can provide either or both of the following capabilities:

* GPU and MIG device allocation through Kubernetes ``ResourceClaim`` objects.
* ComputeDomains for secure `Multi-Node NVLink (MNNVL)
  <https://docs.nvidia.com/multi-node-nvlink-systems/index.html>`_ communication on supported systems.

.. important::

   The DRA operand is disabled by default.
   To use DRA for GPU and MIG allocation, you must disable the NVIDIA Kubernetes Device Plugin because both components
   cannot manage GPU allocation in the same ``ClusterPolicy``.

This page describes the Operator-managed ``ClusterPolicy.spec.draDriver`` operand.
It is distinct from the following deployment paths:

* :doc:`DRA Driver for NVIDIA GPUs <dra-intro-install>` describes installing the driver as a separate Helm release.
  Do not enable ``ClusterPolicy.spec.draDriver`` when you use that standalone deployment.
* The :doc:`GPUCluster Custom Resource Reference <gpucluster-reference>` describes a separate API surface.
  The ``GPUCluster.spec.draDriver`` fields do not configure the ``ClusterPolicy.spec.draDriver`` operand described on
  this page.

Before continuing, become familiar with the `Kubernetes DRA documentation
<https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/>`_ and the
`DRA Driver for NVIDIA GPUs documentation <https://dra-driver-nvidia-gpu.sigs.k8s.io/docs/>`__.

************
Architecture
************

When you enable either DRA capability, the GPU Operator reconciles the ``nvidia-dra-driver-kubelet-plugin`` daemon set
on GPU nodes.
The pod includes a pre-start init container and one or both of the following containers:

* ``gpus`` advertises full GPUs and MIG devices.
* ``compute-domains`` advertises ComputeDomain devices.

When you enable ComputeDomains, the Operator also deploys the ``nvidia-dra-driver-controller`` deployment.
The controller manages ``ComputeDomain`` and ``ComputeDomainClique`` resources and the ComputeDomain daemon pods.

The Operator creates ``DeviceClass`` objects for the enabled capabilities:

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - DeviceClass
     - Capability
   * - ``gpu.nvidia.com``
     - Full GPU allocation.
   * - ``mig.nvidia.com``
     - MIG device allocation.
   * - ``compute-domain-daemon.nvidia.com``
     - ComputeDomain daemon devices.
   * - ``compute-domain-default-channel.nvidia.com``
     - The default ComputeDomain channel.

The GPU and MIG classes are created only when ``draDriver.gpus.enabled=true``.
The ComputeDomain classes and controller are created only when ``draDriver.computeDomains.enabled=true``.

The DRA operand is part of the existing ``ClusterPolicy`` stack.
Other enabled operands, including the NVIDIA GPU driver, NVIDIA Container Toolkit, GPU Feature Discovery, DCGM, and
DCGM Exporter, continue to be managed by the same ``ClusterPolicy``.

*************
Prerequisites
*************

Before you enable the DRA operand, ensure that the following requirements are met:

* Use Kubernetes v1.34.2 or later.
  The cluster must serve the Kubernetes ``DeviceClass`` resource.
  The Operator recognizes ``resource.k8s.io/v1``, ``resource.k8s.io/v1beta2``, and ``resource.k8s.io/v1beta1``.
  Enable the Kubernetes DRA API and its required feature gates when your Kubernetes version does not serve the API by
  default.
  The Helm chart rejects a DRA-enabled installation if it cannot discover a supported ``DeviceClass`` API.
* The nodes and software stack must meet the :ref:`GPU Operator support matrix <operator-platform-support>`.
* Use NVIDIA GPU Driver v580 or later.
  The default driver installed by GPU Operator ${version} meets this requirement.
* Enable Container Device Interface (CDI) in the container runtime.
  The NVIDIA Container Toolkit that the GPU Operator deploys enables CDI by default.
* Node Feature Discovery must run in the cluster.
  The GPU Operator deploys it by default and uses discovered NVIDIA hardware labels to place the DRA kubelet plug-in.

For ComputeDomains, also ensure that:

* NVIDIA Grace Blackwell systems with Multi-Node NVLink, such as NVIDIA HGX GB200 NVL72 or NVIDIA HGX GB300 NVL72,
  are available in the cluster.
* GPU Feature Discovery is enabled so that participating nodes receive the required ``nvidia.com/gpu.clique`` label.
* When you use a pre-installed NVIDIA GPU driver, the matching ``nvidia-imex-*`` packages are installed and the IMEX
  systemd service is disabled on every participating node before you enable the DRA operand.

  .. code-block:: console

     $ systemctl disable --now nvidia-imex.service \
         && systemctl mask nvidia-imex.service

Configuration Restrictions
==========================

The GPU Operator validates both Helm values and the resulting ``ClusterPolicy``.
The following combinations are rejected:

* ``devicePlugin.enabled=true`` with ``draDriver.gpus.enabled=true``.
  Disable the device plug-in when the DRA driver manages GPU and MIG allocation.
* ``sandboxWorkloads.enabled=true`` with either DRA capability enabled.

The device plug-in can remain enabled when only ``draDriver.computeDomains.enabled=true`` because ComputeDomains do
not replace GPU allocation in that configuration.

.. _dra-install:

*******
Install
*******

Choose the capability configuration that meets your requirements:

.. list-table::
   :header-rows: 1
   :widths: 34 22 22 22

   * - Configuration
     - ``devicePlugin.enabled``
     - ``draDriver.gpus.enabled``
     - ``draDriver.computeDomains.enabled``
   * - DRA GPU and MIG allocation
     - ``false``
     - ``true``
     - ``false``
   * - ComputeDomains with device-plugin allocation
     - ``true``
     - ``false``
     - ``true``
   * - DRA GPU and MIG allocation with ComputeDomains
     - ``false``
     - ``true``
     - ``true``

The following steps enable DRA GPU and MIG allocation.
Add ``--set draDriver.computeDomains.enabled=true`` to also enable ComputeDomains.
The commands use the chart defaults, ``clusterPolicy.deployCR=true`` and ``gpuCluster.deployCR=false``.
Do not enable both custom resources in the same installation.

#. Add the NVIDIA Helm repository:

   .. code-block:: console

      $ helm repo add nvidia https://helm.ngc.nvidia.com/nvidia \
          && helm repo update

#. Install or upgrade the GPU Operator:

   .. code-block:: console

      $ helm upgrade --install gpu-operator nvidia/gpu-operator \
          --version=${version} \
          --create-namespace \
          --namespace gpu-operator \
          --set devicePlugin.enabled=false \
          --set draDriver.gpus.enabled=true

   This command uses the default GPU Operator configuration for the GPU driver and other operands.
   If the NVIDIA GPU driver is pre-installed on the nodes, also specify ``--set driver.enabled=false`` as described in
   :doc:`Installing the NVIDIA GPU Operator <getting-started>`.

To enable only ComputeDomains while retaining device-plugin allocation, use the following values instead:

.. code-block:: console

   $ helm upgrade --install gpu-operator nvidia/gpu-operator \
       --version=${version} \
       --create-namespace \
       --namespace gpu-operator \
       --set draDriver.computeDomains.enabled=true

*********************
Validate Installation
*********************

#. Confirm that the ``ClusterPolicy`` reports a ready state:

   .. code-block:: console

      $ kubectl get clusterpolicy

#. Confirm that the kubelet plug-in runs on the expected GPU nodes:

   .. code-block:: console

      $ kubectl get pods -n gpu-operator -l app=nvidia-dra-driver-kubelet-plugin

   The pod reports ``1/1`` when one capability is enabled and ``2/2`` when both capabilities are enabled.

#. If you enabled ComputeDomains, confirm that the controller is running:

   .. code-block:: console

      $ kubectl get pods -n gpu-operator -l app=nvidia-dra-driver-controller

#. List the ``DeviceClass`` objects for the enabled capabilities:

   .. code-block:: console

      $ kubectl get deviceclass

#. Confirm that the DRA driver publishes devices from the GPU nodes:

   .. code-block:: console

      $ kubectl get resourceslices

Use a ``ResourceClaim`` or ``ResourceClaimTemplate`` that references one of the NVIDIA ``DeviceClass`` objects to
request devices for a workload.
The manifest API version depends on the DRA API version that your Kubernetes cluster serves.
For tested GPU, MIG, and ComputeDomain workload examples, refer to the
`DRA Driver for NVIDIA GPUs documentation <https://dra-driver-nvidia-gpu.sigs.k8s.io/docs/>`__.

.. _dra-feature-gates:

**************************
Configure Driver Features
**************************

``draDriver.featureGates`` is a map of feature-gate names and Boolean values that configures the DRA Driver binary.
The GPU Operator renders the map as the ``FEATURE_GATES`` environment variable on the controller and on every enabled
kubelet-plugin container.

These driver feature gates are separate from the Kubernetes feature gates that expose the DRA API.
Supported driver feature-gate names depend on the DRA Driver version included with the GPU Operator release.
Refer to the DRA Driver documentation for the included version before you set this field.

You can set driver feature gates in a values file:

.. code-block:: yaml

   draDriver:
     featureGates:
       <feature-gate-name>: true

For the complete DRA configuration schema and defaults, refer to
:ref:`spec.draDriver <clusterpolicy-spec-dra-driver>` and :ref:`DRA Driver <helm-values-dra>`.

************************
Additional Documentation
************************

* :doc:`DRA Driver for NVIDIA GPUs <dra-intro-install>` — install the DRA driver as a standalone Helm release.
* :doc:`GPUCluster Custom Resource Reference <gpucluster-reference>` — configure the separate ``GPUCluster`` DRA
  integration.
* `DRA Driver for NVIDIA GPUs documentation <https://dra-driver-nvidia-gpu.sigs.k8s.io/docs/>`__
* `Kubernetes DRA documentation
  <https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/>`_
