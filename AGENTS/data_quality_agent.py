from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class DataQualityAgent:
    name: str = "data_quality_agent"
    responsibility: str = "Evaluate completeness, validity, uniqueness, freshness, and declared quality thresholds."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        metrics = dict(case.get("quality_metrics", {})); thresholds = dict(case.get("quality_thresholds", {}))
        failed = [m for m, t in thresholds.items() if float(metrics.get(m, float('-inf'))) < float(t)]
        return {"agent": self.name, "metrics": metrics, "failed": failed, "pass": not failed and bool(metrics)}
