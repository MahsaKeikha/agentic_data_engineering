from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class RecoveryPlanner:
    def plan(self, dataset: str, checkpoint: str, owner: str) -> Dict[str, Any]:
        return {"dataset": dataset, "checkpoint": checkpoint, "owner": owner, "requires_test": True, "approved": False}
