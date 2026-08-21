from typing import Any, Dict

def contract_analysis(contract: Dict[str, Any]) -> Dict[str, Any]:
    required = ["dataset", "owner", "schema", "version"]
    missing = [k for k in required if not contract.get(k)]
    return {"missing": missing, "complete": not missing}
