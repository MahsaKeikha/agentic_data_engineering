from dataclasses import dataclass
from typing import Any, Dict, Iterable

@dataclass
class SchemaValidator:
    def validate(self, record: Dict[str, Any], required_fields: Iterable[str]) -> Dict[str, Any]:
        missing = [f for f in required_fields if f not in record]
        return {"missing": missing, "valid": not missing}
