from dataclasses import dataclass
from typing import Dict

@dataclass
class QualityChecker:
    def compare(self, metrics: Dict[str, float], thresholds: Dict[str, float]) -> Dict[str, object]:
        failed = {k: {"value": metrics.get(k), "threshold": v} for k, v in thresholds.items() if float(metrics.get(k, float('-inf'))) < float(v)}
        return {"failed": failed, "pass": not failed}
