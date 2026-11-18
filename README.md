# Bùi Ngọc Sơn Brain — VTC NEWS (unofficial)

A **standalone**, installable Claude/Codex-style plugin repository modeled on the [Chase Chappell Brain](https://github.com/thomasavada/chase-chappell-brain) package structure. **Not affiliated with or endorsed by TS Bùi Ngọc Sơn or VTC NEWS.** The purpose is to learn the guest's *reasoning*, not impersonate his voice or publish full video transcripts.

## What's inside

- **20** video-ID keyed, timestamp-linked, paraphrased source cards in [`knowledge/sources`](plugins/bui-ngoc-son-knowledge/knowledge/sources/index.md).
- Concept maps for AI/chips/work, economics, and geopolitics/US–China/Trump; a transferable explanation-pattern guide; an evidence contract.
- `/ask-son`, `/teach-son`, `/check-son-claim` commands and corresponding skills. Claims are attributed as guest views, not presented as independently verified facts.
- Public YouTube watch links; **no complete auto-caption files**, private Obsidian vault content, credentials or personal notes.

The 20 reviewed IDs are **not** exhaustive VTC coverage. A name-matched discovery search yielded 520 candidates; 500 have not been promoted to reviewed content. Read [coverage and caveats](plugins/bui-ngoc-son-knowledge/knowledge/foundations/evidence.md).

## Install (Claude Code)

```text
/plugin marketplace add thomasavada/bui-ngoc-son-brain
/plugin install bui-ngoc-son-knowledge@bui-ngoc-son-brain
```

Then ask `/ask-son Chủ đề AI và việc làm`, `/teach-son Giải thích GDP thực và GDP danh nghĩa`, or `/check-son-claim <video URL + timestamp + claim>`.

For local validation: `claude plugin validate .` then `claude plugin validate plugins/bui-ngoc-son-knowledge`. Codex plugin metadata and agent marketplace metadata are included using the Chase Chappell layout; verify your client's marketplace commands against its current documentation.

## Private transcript evidence for faithful reasoning

The public plugin intentionally does **not** redistribute the full YouTube auto-captions. Twenty full caption artifacts are held in the owner's **private** evidence vault. A card-only install can discuss ideas, but must not claim to have learned the guest's speech patterns from a transcript. To attach an authorized *local* archive after cloning this repo, place its 20 JSON files under `plugins/bui-ngoc-son-knowledge/knowledge/.local-transcripts/raw/` (or symlink that directory to your private archive), then run:

```text
python plugins/bui-ngoc-son-knowledge/scripts/prepare-local-excerpts.py --source <your-private-transcript-directory>
```

This produces local-only timestamp windows from five interviews that contrast the **host questions** with the **guest answers**. Both `.local-transcripts/raw/` and `.local-transcripts/excerpts/` are Git-ignored; confirm `git status` before sharing. The skill reads these windows when present and otherwise discloses the card-only limitation. Raw captions are fallible; check audio before claiming an exact quotation or vocal manner. This local companion is not transferred by the marketplace install.

Hermes can use the separate `bui-ngoc-son-vtc-brain` skill backed by that private vault; the Claude marketplace manifest itself is **not** a Hermes-native plugin install.

## Evidence policy

The original videos are the source. These cards paraphrase Vietnamese automatic captions; they do not certify identities, numbers, policy status or contested news. Cite timestamps, separate host narration from guest views, and check consequential current claims independently. If a video is not one of the reviewed source IDs, do not imply the plugin has indexed it.
