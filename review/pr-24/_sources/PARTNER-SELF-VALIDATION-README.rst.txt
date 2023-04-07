.. license-header
  SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
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

.. headings # #, * *, =, -, ^, "

##################################################################
Partner Self-Validated Configurations with the NVIDIA GPU Operator
##################################################################


*******************************************
About Partner Self-Validated Configurations
*******************************************

Refer to
`About Self-Validated Configurations <https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/self-validated/about-self-validated.html>`_
in the product documentation.


************************************************
How to Contribute a Self-Validated Configuration
************************************************

You can contact the NVIDIA team via email (TBD).
NVIDIA will reach out to set up a meeting to discuss the software stack and share
additional details about the program.


************************
What Partners Have to Do
************************

You are asked to provide the following:

* Document and contribute the exact software stack that that you self-validated.
  Refer to the ``PARTNER-SELF-VALIDATION-TEMPLATE.rst`` file as a starting point
  and open a pull request to the repository with your update.
  Refer to the ``CONTRIBUTING.md`` file for information about contributing to the docs.

* Run the self-validated configuration and then share the outcome with NVIDIA by providing
  the output from ``must-gather``.

* Upon request, provide NVIDIA remote access so that the NVIDIA team can perform
  further verification.

* Specify a GitHub username that NVIDIA can refer to when end users open GitHub issues
  specific to the partner self-validated stack.


*****************************
How End Users Receive Support
*****************************

Self-validated configurations receive community support that is provided by the partner.
When an end user experiences an issue with a self-validated configuration and the
NVIDIA GPU Operator, the end user can raise an issue on the NVIDIA GPU Operator
GitHub repository.
NVIDIA adds the partner contact to the GitHub issue so that the partner can work
through the issue.


****************************************
How Partners Receive Support from NVIDIA
****************************************

When the partner is not able to resolve an end user issue without the help from NVIDIA,
the partner is responsible to replicate the issue on one of the software stacks that
NVIDIA supports.

The NVIDIA records the
`supported operating systems and Kubernetes versions <https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/platform-support.html#supported-operating-systems-and-kubernetes-platforms>`_
in the product documentation.

After the steps to reproduce the issue on an NVIDIA supported software stack are recorded,
NVIDIA investigates fixing the issue on the NVIDIA supported software stack.
After NVIDIA develops and releases the fix for the NVIDIA supported software stack,
the partner validates, and, if necessary, ports the fix to the partner software stack.

In cases where the partner provides software, such as GPU driver images, the partner
provides maintenance and support of the software.
This maintenance and support includes security and bug fixes.

