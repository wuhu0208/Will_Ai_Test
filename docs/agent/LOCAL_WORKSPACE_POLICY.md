# Local Workspace Policy

## Purpose and authority

GitHub remote state and latest `main` remain workflow authority. The primary
user-visible local checkout is a convenient mirror of accepted `main`; it is not
Issue, PR, Review, CI, or label authority. These rules make accepted artifacts
visible across sessions without sacrificing Issue isolation or user files.

## Stable checkout roles

- Keep the primary user-visible repository checkout on local `main`, tracking
  `origin/main`. Do not use that checkout as the long-lived home of an Issue
  branch.
- Create or reuse a linked worktree for every Issue branch. A task worktree may
  remain available through review and repair, but its presence does not mean the
  artifact is incomplete.
- Discover actual checkout roles with `git worktree list` and current branch
  readback. Do not infer them from conversation history, a cached path, Finder
  state, or the current shell directory alone.
- Never copy an unmerged canonical deliverable into the primary checkout to make
  it look accepted. It becomes visible there only after the reviewed PR is
  proven merged into remote `main` and the primary checkout is synchronized.

## Post-merge primary-checkout synchronization

After an independently reviewed PR is merged and remote readback proves its
exact head is on `main`, an Agent with access to the primary checkout must:

1. locate the primary checkout using `git worktree list` and verify its branch,
   upstream, tracked changes, untracked files, and ahead/behind state;
2. preserve all user-owned tracked and untracked files; never delete, clean,
   overwrite, auto-stash, or force-reset them;
3. fetch current `origin/main`;
4. ensure the primary checkout is on local `main` without overwriting or
   colliding with local files;
5. update it only by fast-forward (`git merge --ff-only origin/main` or an
   equivalent explicit fast-forward operation);
6. read back the branch, head, upstream, worktree status, and, when applicable,
   the expected merged canonical file under `question_banks/`.

If authentication, network access, branch occupancy, tracked modifications,
untracked-path collision, non-fast-forward history, or an ambiguous primary
checkout prevents a safe update, stop without destructive recovery. Report
`LOCAL_MAIN_SYNC_PENDING` with the exact reason and leave remote workflow state
unchanged. A successful remote merge must not be described as a failed merge
merely because its local mirror is pending.

## Session-independent delivery invariant

The source PDF remains the canonical delivery boundary across all sessions:

- one PDF produces exactly one same-stem canonical Markdown;
- all models and options contained in that PDF stay together in that file;
- distinct PDFs stay distinct even when they represent the same product family
  or duplicate common technical appendices;
- Issue boundaries, worktrees, invocations, scheduler cycles, and conversations
  never split or merge canonical business deliverables.
