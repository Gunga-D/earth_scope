from dataclasses import dataclass

@dataclass
class Destination:
    kilometers: float
    degrees: float
    on_map: str