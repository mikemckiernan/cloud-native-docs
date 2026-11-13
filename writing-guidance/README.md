# Documentation Writing Guidance

This directory preserves editorial guidance and the reviews that explain the guidance.
Read [Writing Preferences](preferences.md) and [Review Examples](examples.md) before drafting documentation.
The NVIDIA style guide remains the authoritative style reference.

## Files

The following files support writing and subsequent review:

- `preferences.md` contains the current guidance, including qualifications from later feedback.
- `examples.md` explains selected revisions and distinguishes accepted wording from proposed applications of feedback.
- `reviews/container-toolkit-1.20.2.jsonl` preserves the 12 review records from the Container Toolkit 1.20.2 experiment.
- `reviews/ctk-1.20.2-draft-b.patch` preserves the initial independent draft.
- `reviews/ctk-1.20.2-draft-b-after-review-012.patch` preserves the cumulative draft after the recorded reviews.
- `reviews/container-toolkit-1.20.2-context.json` identifies the starting commit, style-guide digest, and artifact provenance.
- `reviews/gpu-operator-26.7.3.jsonl` preserves 11 selected review records from the GPU Operator release-note and upgrade-guide review.
- `reviews/gpu-operator-26.7.3-after-review.patch` preserves the reviewed product-documentation changes for context.
- `reviews/gpu-operator-26.7.3-context.json` records source commits, artifact hashes, collection limits, and the elapsed review window.

The patches are historical evidence, not instructions to apply product documentation changes.
The examples illustrate writing decisions, not a technical reference for later releases.
No documentation draft is marked accepted as a whole.

## Recording Review Feedback

Record feedback while performing the requested revision so the reviewer does not need to label examples separately.
Use the following procedure:

1. Append a record to the appropriate task file in `reviews/` with a unique ID and the user's exact feedback.
2. Save the affected file path and the text before and after the revision.
3. Record whether a lesson is an explicit user instruction or an agent inference, and whether revised wording is proposed or explicitly accepted.
4. Link later refinements to earlier record IDs without overwriting the earlier feedback or examples.
5. Update `preferences.md` and `examples.md` when the feedback supplies or refines reusable guidance.

Keep task-specific facts and instructions in the review record rather than turning them into general writing rules.
For example, confirmed Azure Linux architecture coverage is a task fact, not an editorial preference.
Do not promote an inferred lesson to an explicit user instruction without evidence.
If a revision is still proposed, label the example as proposed even when the underlying preference is an explicit instruction.

## Review Record Format

Store one JSON object per line.
Each new record must include the following fields:

- `id`: A unique identifier within the repository.
- `draft`: The draft identifier.
- `recorded_at`: The recording time with a timezone.
- `reviewer`: The source of the feedback.
- `feedback`: The exact feedback, without editorial rewriting.
- `category`: The subject of the feedback.
- `revision_status`: Whether the revised text is proposed or has explicit acceptance evidence.
- `changes`: File paths and the corresponding `before` and `after` text.

Use `refines` for earlier records qualified by the feedback.
Use `reusable_preference` for a stated lesson and `preference_status` to identify its basis.
Use `candidate_lesson` and `candidate_lesson_status` for an agent inference awaiting confirmation.
Record acceptance evidence in `accepted_wording` and `accepted_wording_status` when available.

The imported records retain their original fields and status values.
Record `draft-b-review-009` contains explicit acceptance of one suggested sentence, not approval of the surrounding paragraph or the entire draft.
Records without explicit acceptance remain proposed.
Pre-commit hooks exclude `reviews/` so spelling and whitespace fixes do not alter the recorded evidence.
Artifact hashes in the context file identify the preserved bytes.

## Maintaining the Guidance

Keep the preferences concise enough to read before every writing task.
Keep explanations and contrasting examples in `examples.md`.
Preserve unsuccessful intermediate revisions in the review records, where the sequence explains why a preference changed.
Reference review IDs when updating guidance so another agent can trace each preference to the feedback.
Do not treat recording feedback as evidence that later drafts have improved.
