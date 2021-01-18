.. Date: Jan 17 2021
.. Author: smerla

.. _install-gpu-operator-vgpu:

Considerations To Install GPU Operator with vGPU Driver
-------------------------------------------------------

High Level Workflow
^^^^^^^^^^^^^^^^^^^

The following section outlines the high level workflow to use the GPU Operator with NVIDIA vGPUs.

#. Download the vGPU Software and latest NVIDIA vGPU Driver Catalog file.
#. Clone driver container source repository for building private driver image.
#. Create vGPU license configuration file.
#. Build the driver container image.
#. Push the driver container image to your private repository.
#. Install the GPU Operator.

Detailed Workflow
^^^^^^^^^^^^^^^^^

Download the vGPU Software and latest NVIDIA vGPU catalog driver file from the NVIDIA Licensing Portal.

#. Login to the NVIDIA Licensing Portal and navigate to the “Software Downloads” section.
#. The NVIDIA vGPU Software is located in the Software Downloads section of the NVIDIA Licensing Portal.
#. The NVIDIA vGPU catalog driver file is located in the “Additional Software” section.
#. The vGPU Software bundle is packaged as a zip file. Extract the zip file

Clone the driver container repository and build driver image

* Open a terminal and clone the driver container image repository

.. code-block:: console

    $ git clone https://gitlab.com/nvidia/container-images/driver
    $ cd driver

* Change to the OS directory under the driver directory

.. code-block:: console

    $ cd ubuntu20.04

* Copy the vGPU guest driver from your extracted zip file and the vGPU driver catalog file

.. code-block:: console

    $ cp <local-driver-download-directory>/*.run drivers
    $ cp vgpuDriverCatalog.yaml drivers

* Create vGPU license configuration file

Create a vGPU license file named `gridd.conf` in the drivers/ folder with the below content.

.. code-block:: text

    # Description: Set License Server Address
    # Data type: string
    # Format:  "<address>"
    ServerAddress=<license server address>

Input the license server address of the License Server

* Build the driver container image

Set the private registry name using below command on the terminal

.. code-block:: console

    $ export PRIVATE_REGISTRY=<private registry name>

Set the OS_TAG. The OS_TAG has to match the Guest OS version. Supported values are ubuntu20.04, ubuntu18.04, rhcos4.5, rhcos4.6

.. code-block:: console

    $ export OS_TAG=ubuntu20.04

Set the driver container image version to a user defined version number. For example 1.0.0

.. code-block:: console

    $ export VERSION=1.0.0
    $ export VGPU_DRIVER_VERSION=460.16-grid (replace this with the guest vgpu grid driver version downloaded from NVIDIA software portal)

.. note::

    ``VERSION`` can be any user defined value. Please note this value to use during operator installation command

Build the driver container image

.. code-block:: console

    $ sudo docker build --build-arg DRIVER_TYPE=vgpu --build-arg VGPU_LICENSE_SERVER_TYPE=FNE --build-arg DRIVER_VERSION=$VGPU_DRIVER_VERSION -t ${PRIVATE_REGISTRY}/driver:${VERSION}-${OS_TAG} .

.. note::

    ``VGPU_LICENSE_SERVER_TYPE`` can be of either **FNE** (default) or **NLS** based on licensing server config.

* Push the driver container image to your private repository

.. code-block:: console

    $ sudo docker login ${PRIVATE_REGISTRY} --username=<username> {enter password on prompt}
    $ sudo docker push ${PRIVATE_REGISTRY}/vgpudriver:${VERSION}-${OS_TAG}

* Install the GPU Operator.

Creating an image pull secrets

.. code-block:: console

    $ kubectl  create namespace gpu-operator-resources
    $ export REGISTRY_SECRET_NAME=registry-secret
    $ kubectl create secret docker-registry ${REGISTRY_SECRET_NAME} --docker-server=${PRIVATE_REGISTRY} --docker-username=<username> --docker-password=<password> --docker-email=<email-id> -n gpu-operator-resources

.. note::

    Please note the secret name ``REGISTRY_SECRET_NAME`` for using during operator installation command.

* Install GPU Operator helm chart

Please refer to `install-gpu-operator`_ section for GPU operator installation command and options for vGPU.