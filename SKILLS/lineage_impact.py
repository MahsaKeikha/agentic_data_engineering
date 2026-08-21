from typing import Any, Dict

def lineage_impact(lineage: Dict[str, Any]) -> Dict[str, Any]:
    downstream = list(lineage.get("downstream", []))
    return {"downstream_consumers": downstream, "impact_count": len(downstream), "requires_consumer_review": bool(downstream)}
