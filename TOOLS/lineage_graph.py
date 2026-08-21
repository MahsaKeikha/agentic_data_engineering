from dataclasses import dataclass, field
from typing import Dict, List, Set

@dataclass
class LineageGraph:
    edges: Dict[str, Set[str]] = field(default_factory=dict)

    def add_edge(self, source: str, target: str) -> None:
        self.edges.setdefault(source, set()).add(target)

    def downstream(self, source: str) -> List[str]:
        return sorted(self.edges.get(source, set()))
