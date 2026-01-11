from dataclasses import dataclass, field

@dataclass
class Card:
    id: int
    name: str
    type: str
    age: int = 0
