from dataclasses import dataclass

@dataclass
class Connection:
    host: str
    port: str
    
@dataclass
class Service:
    name: str
    has_supported_scrap: bool
    has_supported_dist: bool
    connection: Connection