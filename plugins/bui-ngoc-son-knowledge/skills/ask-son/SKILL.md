---
name: ask-son
description: Use when asking about TS Bùi Ngọc Sơn’s VTC NEWS interviews. Attribute arguments with timestamps and distinguish verified facts.
---
# Ask Sơn — source-grounded synthesis

Use only for the interviewed expert **TS Bùi Ngọc Sơn**, not other people named Sơn. Find this plugin’s `knowledge/index.md` relative to the skill directory (`../../knowledge/index.md`) and read `knowledge/foundations/evidence.md` plus relevant concept and source cards. **When local transcript evidence exists, read the matching `knowledge/.local-transcripts/excerpts/<video-id>.md` before writing and, if necessary, inspect the full JSON at `knowledge/.local-transcripts/raw/<video-id>*.json`; never confuse a host question with the guest's answer.** The public package contains 20 paraphrased cards but no full video transcripts. On a machine without local evidence, state that the answer comes from cards only; do not claim you heard him. Search outside the plugin only when asked or when a claim requires independent verification; identify those external sources separately.

Answer in the user's language (Vietnamese by default). Format: (1) what the guest argues with video timestamp URLs, (2) causal mechanism and scope/uncertainty, (3) what is independently verified vs not verified. Present no fabricated quotations. Do not equate a presenter’s editorial frame with the guest’s views. For a question beyond reviewed cards, state the corpus does not cover it. Never claim to be TS Bùi Ngọc Sơn or endorsed by him.
