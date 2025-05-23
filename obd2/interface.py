import serial
import time
import re
from obd2.pids import PID


class Obd2Interface:
    def __init__(self, config):
        self.port = config.port
        self.baudrate = config.baudrate
        self.connection = None

    def connect_elm327(self):
        """Try to connect to ELM327."""
        try:
            self.connection = serial.Serial(self.port, self.baudrate, timeout=1)
            print(f"Connected to ELM327 at {self.port} with baudrate {self.baudrate}")
        except serial.SerialException as e:
            raise ValueError(f"[error]: Failed to connect to ELM327: {e}")

    def disconnect_elm327(self):
        """Disconnect from ELM327."""
        try:
            self.connection.close()
            print("Disconnected from ELM327")
        except serial.SerialException as e:
            raise ValueError(f"[error]: Failed to disconnect from ELM327: {e}")

    def send_elm_command(self, command):
        """Send command to ELM327 and return response."""

        try:
            self.connection.write(f"{command}\r".encode("ascii"))
            time.sleep(0.1)
            response = ""

            while True:
                char = self.connection.read().decode("ascii", errors="ignore")
                if char == ">":
                    break

                response += char
                if not char and not self.connection.in_waiting:
                    break

            clean_response = response.replace(command, "")
            clean_response = re.sub(r"[\r\n]", "", clean_response)
            clean_response = re.sub(r"\d+:", "", clean_response)
            clean_response = re.sub(r"\s+", " ", clean_response)
            clean_response = clean_response.strip()

            return clean_response
        except serial.SerialException as e:
            raise ValueError(f"[error]: Failed to send command '{command}': {e}")
        except UnicodeDecodeError as e:
            raise ValueError(
                f"[error]: Failed to decode command response: '{command}:{e}'"
            )
        except Exception as e:
            raise ValueError(f"[error]: Unexpected error: {e}")

    def parse_pid_response(self, pid: PID, raw_response: str):
        """Decode raw response from OBD2 using PID formula."""
        try:
            data_hex = raw_response.split(" ")
            data_hex = data_hex[(len(data_hex) - pid.bytes) :]
            data_hex_str = "".join(data_hex)

            # Convert hexadecimal string to bytes
            data_bytes = [
                int(data_hex_str[i : i + 2], 16) for i in range(0, len(data_hex_str), 2)
            ]

            try:
                value = pid.formula(*data_bytes)
            except Exception as e:
                print(f"Erro ao calcular fórmula do PID {pid}: {e}")
                value = None

            return value
        except Exception as e:
            raise ValueError(
                f"[error]: Error parsing PID response: {pid.command}, Raw response: {raw_response}, Error: {e} "
            )
