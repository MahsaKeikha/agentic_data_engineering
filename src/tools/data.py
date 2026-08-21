def contract_record(c):return {"schema":c.get("schema"),"owner":c.get("owner"),"sla":c.get("sla")}
def lineage_graph(c):return {"sources":c.get("sources",[]),"lineage":c.get("lineage",[]),"consumers":c.get("consumers",[])}
def quality_report(c):return {"checks":c.get("quality_checks",[]),"failures":c.get("quality_failures",[])}
def transformation_plan(c):return {"transformations":c.get("transformations",[]),"tests":c.get("transformation_tests",[])}
def reliability_plan(c):return {"schedule":c.get("schedule"),"retry":c.get("retry"),"recovery":c.get("recovery")}
TOOL_MANIFEST=[{"name":n,"side_effects":False} for n in ("contract_record","lineage_graph","quality_report","transformation_plan","reliability_plan")]
