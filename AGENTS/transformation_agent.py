from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class TransformationAgent:
    name: str = "transformation_agent"
    responsibility: str = "Review transformation logic, tests, idempotency, dependencies, and expected outputs."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        t = case.get("transformation", {})
        return {"agent": self.name, "name": t.get("name"), "tests_passed": bool(t.get("tests_passed")), "idempotent": bool(t.get("idempotent")), "ready": bool(t.get("name") and t.get("tests_passed") and t.get("idempotent"))}
