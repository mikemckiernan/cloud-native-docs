# Review Examples

These examples explain decisions from the Container Toolkit 1.20.2 and GPU Operator 26.7.3 reviews.
Use the editorial lessons, not the product facts, when writing about another feature or release.
Review IDs refer to the preserved [Container Toolkit feedback](reviews/container-toolkit-1.20.2.jsonl) and [GPU Operator feedback](reviews/gpu-operator-26.7.3.jsonl).

## Remove Unnecessary Product Version Framing

The reviewer instructed the agent to describe behavior directly because the guides are versioned.
The revised wording below remains a proposed application of that instruction.

Before:

> As of version 1.20.2, generated CDI specifications include a `void` volume mount.

Revised:

> Generated CDI specifications include a `void` volume mount.

Keep version requirements that readers need to perform a task.
Do not apply this edit to release notes merely because release notes compare versions.

Source: `draft-b-review-001`.

## Restate the Subject Without Repeating Its Function

The first correction asked the agent to replace vague references with nouns where natural.
The next correction explained that the agent had repeated too much information.

Original:

> This applies when `accept-nvidia-visible-devices-as-volume-mounts` is enabled.

Overcorrection:

> The `void` mount suppresses volume-mount device requests when `accept-nvidia-visible-devices-as-volume-mounts` is enabled.

The preceding sentence already explained the mount's function.
Repeating that explanation added unnecessary detail.
The reviewer suggested shortening the sentence to "The `void` mount is added when…".
Checking the implementation showed that adding the mount is unconditional, while its effect on volume-mount requests depends on the setting.
Do not change that distinction while simplifying the prose.

Later proposed wording:

> Generated CDI specifications include a `void` volume mount.
> When you set `accept-nvidia-visible-devices-as-volume-mounts` to `true`, the `void` mount prevents the NVIDIA Container Runtime from injecting additional devices through volume-mount requests.
> The setting defaults to `false`.

The configuration clarification is part of this example's technical context.
It has not been promoted to a separate writing rule.

Sources: `draft-b-review-003` through `draft-b-review-006`.

## Explain the Outcome Instead of Renaming the Mechanism

The reviewer rejected anthropomorphic wording about applications seeing GPUs.
The agent first substituted "visibility" and then suggested "enumeration".
The reviewer asked what the reader ultimately wanted to accomplish.

Original:

> EGL and Vulkan applications can see only the physical GPUs assigned to the container.

Intermediate revision:

> GPU visibility for EGL and Vulkan applications is limited to the physical GPUs assigned to the container.

Explicitly accepted wording:

> The application profile configures EGL and Vulkan applications to use the physical GPUs assigned to the container.

The accepted sentence explains the intended use of the assigned GPUs.
It does not claim that the application profile grants device permissions.
The acceptance applies to this sentence, not the entire documentation draft.

Sources: `draft-b-review-008` and `draft-b-review-009`.

## Explain the Affected Configuration in Release Notes

The reviewer asked what problem the `void` mount solved and whether configuration affected the behavior.

Original:

> Generated CDI specifications now prevent duplicate device injection when the NVIDIA Container Runtime accepts device requests through volume mounts.
> The specification adds a `void` volume mount that suppresses volume-mount device requests, so the runtime does not inject devices in addition to the CDI-selected devices.

Proposed revision:

> Fixed an issue where volume-mount requests could add GPUs to a container in addition to the GPUs selected through CDI.
> This issue affected configurations with `accept-nvidia-visible-devices-as-volume-mounts` set to `true`.
> The setting defaults to `false`.

The revision identifies the problem and the affected configuration.
The original fix describes the device-injection problem but does not link a user-reported application failure.
Do not invent such a failure to make the release note more compelling.

Source: `draft-b-review-010`.

## Retain the Example and Consequence After Removing Internals

The reviewer found "built-in applet" distracting.
Removing that detail alone left the change vague, so the reviewer requested an example and the reason the change matters.

Original:

> The toolkit container now uses a BusyBox build that runs host binaries when executing commands through `chroot`.
> Previously, BusyBox could run a built-in applet instead of the requested host binary.

Too terse:

> Commands run through `chroot` in the toolkit container now execute the host binaries.

Proposed revision after the refinement:

> Commands run through `chroot` in the toolkit container now execute host binaries, such as `modprobe`, so kernel modules and their dependencies load correctly.

The example and consequence explain the value of the change without detailing BusyBox command dispatch.
The revised sentence remains proposed.

Sources: `draft-b-review-011` and `draft-b-review-012`.

## State the Current Restriction Directly

The reviewer found the explanation of automatic module selection tentative and poorly connected to the following version qualification.

Before:

> You can use `kernelModuleType: auto` to let the driver container select the kernel module type.
> GDS versions that require open kernel modules cannot use `kernelModuleType: proprietary`.
> GDS is not supported with precompiled drivers.

Applied revision, without separate explicit acceptance of this exact wording:

> GDS is not supported with precompiled drivers or with `kernelModuleType: proprietary`.

This illustrates a restriction for the reviewed release, not a claim about every historical GDS version.
The broader lesson of stating applicable restrictions directly is an agent interpretation of the feedback.

Sources: `gpu-operator-review-002` and `gpu-operator-review-003`.

## Prefer a Verb That Describes the Behavior

Before:

> A startup probe now allows up to five minutes for initialization before liveness checks begin.

Explicitly accepted wording:

> The startup probe waits up to five minutes for initialization to complete before liveness checks begin.

The reviewer requested this specific replacement.
The record does not establish a universal ban on "allows".
The five-minute limit was checked against the probe settings and regression tests.

Sources: `gpu-operator-review-005` and `gpu-operator-review-007`.

## Explain Monitoring Behavior Before Naming Its Output

An intermediate proposal named the output metrics before establishing why readers needed the identifier:

> The resulting `accelerator_*` metrics retain their existing names, values, and units, preserving compatibility with dashboards and alerts that use them.

Explicitly accepted wording, with the preceding sentence for context:

> On OpenShift, the Operator's GPU monitoring rules support both the previous and renamed metrics.
> Existing metric names, values, and units are preserved for dashboards and alerts.

The reviewer questioned the identifier and explicitly requested the simpler proposal.
The inference is that an identifier should earn its place by helping the reader understand or perform the task.
This does not establish a general prohibition on metric names.

Source: `gpu-operator-review-004`.

## Distinguish Recommended Defaults from Accepted Configuration

The reviewer preferred removing legacy device-list strategies rather than describing combinations merely because they pass validation.
The migrated guidance recommends removing legacy overrides to use the Operator's defaults, or explicitly choosing the default CDI strategies.
The revised wording has no separate explicit acceptance evidence.

A candidate lesson is to lead with recommended configurations and distinguish them from the broader set accepted by validation.
This generalization remains an agent interpretation, not a confirmed rule for every configuration task.

Source: `gpu-operator-review-001`.

## Keep a Workaround Visible Until the Shipped Configuration Resolves the Issue

The original draft classified uncompressed image layers as a fixed issue.
The reviewer explained that the workaround made that classification misleading, even if the cause had been fixed in code.
The entry moved to known issues.

An intermediate revision proposed a workaround reported in the GitHub issue.
The reviewer then recalled the engineering-supported image override and asked the agent to verify and align with that advice.
The final entry explains the Driver Manager override and its workload-disruption consequence.
The image tag remains a release-validation detail, not reusable writing guidance.

The reviewer subsequently clarified that proposing the issue originator's workaround was not a concern.
Do not turn this sequence into a rule that excludes reporter-supplied workarounds.
The record preserves the intermediate revision without presenting it as an editorial failure.

Sources: `gpu-operator-review-006`, `gpu-operator-review-008`, and `gpu-operator-review-009`.

## Apply the Decision to Related Task Guidance

After reviewing the release notes, the reviewer asked whether the upgrade page needed corresponding edits and requested the proposed changes.
The upgrade page gained a warning about Driver Manager image changes evicting workloads and a clearer DCGM rollback explanation.
Release-specific image tags remained in the release notes.
This reinforces the existing instruction to apply corrections to comparable passages within the task scope.

Source: `gpu-operator-review-010`.
