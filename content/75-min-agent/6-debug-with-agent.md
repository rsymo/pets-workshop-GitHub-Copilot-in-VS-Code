# 6 — Debug with Agent (8–10 min)

Goal: Reproduce and fix an intentional bug. Use @tests and @workspace.

Seeded failure idea:
- Backend returns status as value but frontend expects name (or vice versa). Or a 400 on missing id.

Prompts:
- “@workspace Find the mismatch causing the UI to fail to update favorites. Propose a minimal fix.”
- “Apply the diff; re-run tests; verify UI.”
