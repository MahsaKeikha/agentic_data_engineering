def review_contract(a):return {**a,"questions":([] if a.get("schema") else ["Data schema/contract is missing"])}
def analyze_lineage(a):return {**a,"questions":([] if a.get("lineage") else ["Lineage evidence is missing"])}
def evaluate_quality(a):
 q=[] if a["checks"] else ["Data quality checks are missing"]
 r=["Quality failure: "+str(x) for x in a["failures"]]
 return {**a,"questions":q,"risks":r}
def review_transformations(a):return {**a,"risks":([] if a["tests"] else ["Transformation tests are missing"])}
def assess_reliability(a):return {**a,"risks":([] if all(a.values()) else ["Orchestration/recovery controls are incomplete"])}
SKILL_MANIFEST=["review_contract","analyze_lineage","evaluate_quality","review_transformations","assess_reliability"]
