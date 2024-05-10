from dataclasses import dataclass

@dataclass
class Stream:
    network: str
    station: str
    channels: list