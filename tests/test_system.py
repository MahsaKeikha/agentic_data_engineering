from src.system import run_system
def case():return {"schema":"s","owner":"team","sla":"daily","sources":["a"],"lineage":["a->b"],"consumers":["c"],"quality_checks":["not-null"],"quality_failures":[],"transformations":["t"],"transformation_tests":["pass"],"schedule":"daily","retry":"3","recovery":"checkpoint"}
def test_clean_waits():assert run_system(case())["status"]=="awaiting_human_approval"
def test_clean_approval():assert run_system(case(),True)["status"]=="approved_for_human_follow_through"
def test_missing_lineage_blocks():
 c=case();c["lineage"]=[];assert run_system(c,True)["status"]=="blocked"
def test_quality_failure_blocks():
 c=case();c["quality_failures"]=["duplicate key"];assert run_system(c,True)["status"]=="blocked"
