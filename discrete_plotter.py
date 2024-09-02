from dataclasses import dataclass
import matplotlib.pyplot as plt

@dataclass
class DamageResult:
    partner: str
    ability: str
    total_damage: int

    def __repr__(self) -> str:
        return f'{self.partner}|{self.ability}:{self.total_damage} damage'