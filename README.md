# F33 Agentic Data Engineering

Standalone multi-agent reference system for data contracts, lineage, quality, transformation, orchestration, and reliability review.

## Architecture

```text
src/
├── agents/          Data Contract, Lineage, Quality, Transformation, Reliability agents
├── tools/           deterministic data-inspection and planning helpers
├── skills/          reusable data-engineering procedures
├── memory/          pipeline memory
├── schemas/         contract fields and evidence contracts
├── prompts/         engineering principles
├── config/          reference configuration
├── safety/          publication/handoff policy
├── observability/   trace summaries
├── state.py
├── gates.py
├── orchestrator.py
├── system.py
└── run.py
```

### Agents
Data Contract Agent, Lineage Agent, Data Quality Agent, Transformation Agent, Reliability Agent, coordinated by the Data Engineering Orchestrator.

### Skills
Contract review, lineage analysis, quality evaluation, transformation review, reliability assessment.

### Tools
Contract record, lineage graph, quality report, transformation plan, reliability plan.

See `docs/AGENTS_TOOLS_SKILLS.md`.

```bash
python -m src.run --example
pytest -q
```

Missing lineage, failed quality evidence, absent transformation tests, conflicts, or incomplete recovery controls block clean handoff.

**Maturity: Reference implementation.** Production pipelines require platform-specific security, privacy, access control, scale, recovery, and operational validation.

AI Engineering Handbook Series by Mahsa Keikha:
- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H
