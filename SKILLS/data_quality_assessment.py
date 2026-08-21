from typing import Dict

def data_quality_assessment(metrics: Dict[str, float], thresholds: Dict[str, float]) -> Dict[str, object]:
    failures = [k for k, t in thresholds.items() if float(metrics.get(k, float('-inf'))) < float(t)]
    return {"failures": failures, "pass": not failures and bool(metrics)}
