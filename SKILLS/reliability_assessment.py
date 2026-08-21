from typing import Any, Dict

def reliability_assessment(reliability: Dict[str, Any]) -> Dict[str, Any]:
    required = ["owner", "recovery_plan", "freshness_slo", "monitoring"]
    missing = [k for k in required if not reliability.get(k)]
    return {"missing": missing, "ready": not missing}
