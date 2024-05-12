from dataclasses import dataclass

@dataclass
class GeoserviceStream:
    network: str
    station: str

@dataclass
class LoadedStream:
    network: str
    station: str
    channel: str