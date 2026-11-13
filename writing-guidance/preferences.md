# Writing Preferences

Apply these preferences alongside the authoritative NVIDIA style guide and the task instructions.
These preferences come from the Container Toolkit 1.20.2 and GPU Operator 26.7.3 documentation reviews.
Review IDs refer to the preserved [Container Toolkit feedback](reviews/container-toolkit-1.20.2.jsonl) and [GPU Operator feedback](reviews/gpu-operator-26.7.3.jsonl).

## Describe the Documented Release Directly

In versioned guides, state the behavior of the documented release directly.
Omit introductions such as "As of version 1.20.2" when the documentation version already provides that context.
Put product release history in release notes or migration guidance where comparisons are needed.
Preserve dependency requirements and versions needed to perform a task.

Sources: `draft-b-review-001` and `gpu-operator-review-002`.

## Use One Sentence per Source Line

Write each complete prose sentence on its own source line.
Do not hard-wrap a sentence across lines or put multiple sentences on one line.
Preserve paragraph breaks, list indentation, tables, and code formatting.

Source: `draft-b-review-002`.

## Restate Nouns Without Repeating Explanations

Prefer a specific noun when a pronoun or vague reference requires readers to track earlier subjects.
Repeat only enough of the noun to identify the subject.
Do not repeat the explanation or function already supplied by the preceding sentence.
Retain pronouns where the reference is clear and repeating the noun would be awkward.

Sources: `draft-b-review-003` and its refinement, `draft-b-review-004`.

## Focus on Reader Actions and Outcomes

Describe what readers do and what they can accomplish.
Prefer direct wording such as "When you set…" over "When the setting is set…".
Explain the practical outcome instead of stopping at an abstract mechanism such as GPU visibility or enumeration.
Preserve the technical meaning when changing the explanation.

Sources: `draft-b-review-006` and `draft-b-review-009`.

## Avoid Anthropomorphism

Do not ascribe human qualities to software, applications, or other inanimate objects.
Replace wording such as "applications can see" with a precise explanation of the reader-relevant outcome.
Use engineering sources to establish the behavior, then apply editorial judgment to the explanation.
Do not copy an anthropomorphism merely because an engineering source uses it.

Sources: `draft-b-review-008` and `draft-b-review-009`.

## Explain the Problem in Bug-Fix Release Notes

Lead with the problem affecting readers and the configuration in which the problem occurs.
Explain the corrected outcome before implementation details.
Verify the problem from source material rather than inventing an application failure or user report.

Source: `draft-b-review-010`.

## Classify Issues by the Shipped Behavior

Do not describe an issue as fixed solely because a source-code change has merged.
If the documented configuration still requires a workaround, describe the remaining limitation under known issues and explain the required action.
Include consequences of the workaround, such as workload eviction during an image upgrade.
Verify which workaround applies to the release.
This review does not establish a prohibition on proposing workarounds supplied by issue reporters.

Sources: `gpu-operator-review-006`, its revision in `gpu-operator-review-008`, and the qualification in `gpu-operator-review-009`.

## Keep Details That Explain Why a Change Matters

Omit implementation terms that distract from the changed behavior.
Retain concrete examples and practical consequences that help readers understand why the change matters.
For example, naming `modprobe` and explaining kernel-module dependency handling is more useful than describing BusyBox built-in applets.
Concision must not leave a release note vague or apparently unnecessary.

Sources: `draft-b-review-011`, its refinement, `draft-b-review-012`, and `gpu-operator-review-011`.
