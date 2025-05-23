from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class PID:
    command: str
    bytes: int
    formula: Callable
    unit: str


PIDS = {
    "VIN": PID(
        "0902", 17, lambda *args: bytes(args).decode("ascii"), "Chassi do veículo"
    ),
    "RPM": PID("010C", 2, lambda *args: (256 * args[0] + args[1]) / 4, "RPM"),
    "Velocidade": PID("010D", 1, lambda *args: args[0], "km/h"),
}
