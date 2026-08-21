from dataclasses import dataclass
from typing import Any, Callable, Iterable, List

@dataclass
class TransformationRunner:
    def run(self, records: Iterable[Any], transform: Callable[[Any], Any]) -> List[Any]:
        return [transform(record) for record in records]
