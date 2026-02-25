from dataclasses import dataclass

@dataclass
class Job:
    title: str
    description: str
    website: str = "Indeed"