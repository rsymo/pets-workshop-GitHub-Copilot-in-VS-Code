# Facilitator guide (timeboxes and checkpoints)

- 0–5: Kickoff and warm-up. Tag: 75m-00.
- 5–13: Plan with Copilot. Tag: 75m-01.
- 13–18: Create issues with MCP. Tag: 75m-01a.
- 18–33: Agent implements backend + tests. Tag: 75m-02..03.
- 33–42: Agent fixes tests to green. Tag: 75m-03.
- 42–57: Agent wires frontend. Tag: 75m-04..05.
- 57–67: Debug with Agent. Tag: 75m-06.
- 67–75: Open PR with Copilot. Tag: 75m-07.

Have helper branches ready for each checkpoint.

## Checkpoints and tags

Use annotated tags so attendees can catch up:

- 75m-00 warmup ready
- 75m-01 plan and issues created
- 75m-02 backend stubs
- 75m-03 tests green
- 75m-04 frontend stub
- 75m-05 ui working
- 75m-06 debug
- 75m-07 pr opened

Create a tag:

```
./scripts/create-checkpoint-tag.sh 75m-03 "Tests green"
```

## Intentional bug toggle

For the debug segment, run the backend with the bug enabled:

- VS Code task: “Start Backend (with bug)”
- Or env var:

```
WORKSHOP_INTENTIONAL_BUG=1 python -m flask run --app server.app --host 0.0.0.0 --port 5100
```
