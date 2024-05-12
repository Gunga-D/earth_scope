from dataclasses import dataclass

@dataclass
class ScrapedData:
    file: str
    waveform_data: str
    waveform_format: str