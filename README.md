# F33 Agentic Data Engineering

Standalone multi-agent reference system for data contracts, lineage, quality, transformation, orchestration, and reliability review.

## Agent team

- Data Contract Agent
- Lineage Agent
- Data Quality Agent
- Transformation Agent
- Reliability Agent
- Data Engineering Orchestrator

The **actual specialist agent implementations live in [`src/agents.py`](src/agents.py)**. Shared state, evidence handling, and orchestration live in [`src/system.py`](src/system.py). Agent-composition and workflow tests live under [`tests/`](tests/).

## Architecture

```text
Data contract
   ↓
Contract Agent
   ↓
Lineage Agent
   ↓
Quality Agent
   ↓
Transformation Agent
   ↓
Reliability Agent
   ↓
Data Engineering Orchestrator / Human Gate
```

Missing lineage, failed quality evidence, or incomplete recovery controls remain visible and block a clean handoff.

```bash
python -m src.run --example
pytest -q
```

**Maturity: Reference implementation.** Production pipelines require platform-specific security, privacy, access control, scale, recovery, and operational validation.

## AI Engineering Handbook Series

By Mahsa Keikha:
- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H

MIT licensed.
