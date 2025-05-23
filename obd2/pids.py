from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class PID:
    command: str
    bytes: int
    formula: Callable
    unit: str


PIDS = {
    "RPM": PID("010C", 2, lambda A, B: (256 * A + B) / 4, "RPM"),
    "Velocidade": PID("010D", 1, lambda A: A, "km/h"),
    "Consumo_L_h": PID("015E", 2, lambda A, B: (256 * A + B) / 20, "L/h"),
}
