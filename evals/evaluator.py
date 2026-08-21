def evaluate_result(r):
 a=r.get("analyses",{});return {"contract_present":"data_contract" in a,"lineage_present":"lineage" in a,"quality_present":"quality" in a,"reliability_present":"reliability" in a,"blocked":r.get("status")=="blocked","trace_steps":len(r.get("trace",[]))}
