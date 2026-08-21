from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"AGENTS": ["data_contract_agent.py", "lineage_agent.py", "data_quality_agent.py", "transformation_agent.py", "reliability_agent.py"], "TOOLS": ["schema_validator.py", "lineage_graph.py", "quality_checker.py", "transformation_runner.py", "recovery_planner.py"], "SKILLS": ["contract_analysis.py", "lineage_impact.py", "data_quality_assessment.py", "transformation_planning.py", "reliability_assessment.py"]}
def test_visible_components_exist_and_compile():
    for folder, names in EXPECTED.items():
        for name in names:
            path = ROOT / folder / name
            assert path.exists(), path
            compile(path.read_text(), str(path), "exec")
