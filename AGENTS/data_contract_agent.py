from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class DataContractAgent:
    name: str = "data_contract_agent"
    responsibility: str = "Validate producer/consumer contracts, schema expectations, ownership, and compatibility requirements."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        contract = case.get("contract", {})
        required = ["dataset", "owner", "schema", "version"]
        missing = [k for k in required if not contract.get(k)]
        return {"agent": self.name, "missing": missing, "valid": not missing}
