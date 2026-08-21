from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class ReliabilityAgent:
    name: str = "reliability_agent"
    responsibility: str = "Assess retries, recovery, freshness SLOs, ownership, observability, and failure handling."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        r = case.get("reliability", {})
        required = ["owner", "recovery_plan", "freshness_slo", "monitoring"]
        missing = [k for k in required if not r.get(k)]
        return {"agent": self.name, "missing": missing, "ready": not missing}
