from dataclasses import dataclass

@dataclass
class LoadedData:
    file: str
    waveform_data: str
    waveform_format: str