import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()


@dataclass(frozen=True)
class Obd2Config:
    """
    OBD2 configuration class.
    """

    port: str = os.getenv("OBD2_SERIAL_PORT", "/dev/ttyUSB0")
    baudrate: int = int(os.getenv("OBD2_SERIAL_BAUDRATE", 38400))


@dataclass(frozen=True)
class Settings:
    """
    Settings class.
    """

    obd2: Obd2Config = Obd2Config()


settings = Settings()
