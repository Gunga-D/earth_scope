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

@dataclass
class StationInfo:
    name: str
    latitude: float
    longitude: float

@dataclass
class SeedlinkConnectionInfo:
    host: str
    port: str