from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class LineageAgent:
    name: str = "lineage_agent"
    responsibility: str = "Trace upstream sources, transformations, downstream consumers, and change impact."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        lineage = case.get("lineage", {})
        return {"agent": self.name, "upstream": list(lineage.get("upstream", [])), "downstream": list(lineage.get("downstream", [])), "transformations": list(lineage.get("transformations", [])), "complete": bool(lineage.get("upstream") and lineage.get("downstream"))}
