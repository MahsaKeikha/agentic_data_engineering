# F33 Agentic Data Engineering

Standalone multi-agent reference system for data contracts, lineage, quality, transformation, orchestration, and reliability review.

## Repository map

```text
.github/workflows/tests.yml
src/agents.py
src/state.py
src/gates.py
src/orchestrator.py
src/system.py
src/run.py
evals/evaluator.py
examples/pipeline_case.json
benchmarks/README.md
docs/ARCHITECTURE.md
tests/
SECURITY.md
CONTRIBUTING.md
CITATION.cff
CHANGELOG.md
CODE_OF_CONDUCT.md
LICENSE
pyproject.toml
```

## Multi-agent team
Data Contract Agent, Lineage Agent, Data Quality Agent, Transformation Agent, Reliability Agent, and Data Engineering Orchestrator.

```bash
python -m src.run --example
pytest -q
```

Missing lineage, failed quality evidence, absent transformation tests, conflicts, or incomplete recovery controls block clean handoff.

**Maturity: Reference implementation.** Production pipelines require platform-specific security, privacy, access control, scale, recovery, and operational validation.

AI Engineering Handbook Series by Mahsa Keikha:
- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H
