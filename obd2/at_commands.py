from dataclasses import dataclass


@dataclass(frozen=True)
class AT:
    command: str
    description: str = ""


AT_COMMANDS = {
    "ATZ": AT("ATZ", "Reset the module to factory defaults"),
    "ATE0": AT("ATE0", "Echo off"),
    "ATL1": AT("ATL1", "Line feed on"),
    "ATSP0": AT("ATSP0", "Set Protocol 0 - Auto"),
}
