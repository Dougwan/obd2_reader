import time
from config.settings import Obd2Config
from obd2.pids import PIDS
from obd2.interface import Obd2Interface
from obd2.at_commands import AT_COMMANDS


def start_interface(interface: Obd2Interface):
    try:
        interface.connect_elm327()
    except ValueError as e:
        raise ValueError(e)


def stop_interface(interface: Obd2Interface):
    try:
        interface.disconnect_elm327()
    except ValueError as e:
        raise ValueError(e)


def start_at_commands(interface: Obd2Interface):
    for command, at_command in AT_COMMANDS.items():
        print(f"Sending {command}: {at_command.description}")
        response = interface.send_elm_command(command)
        print(f"Response: {response}")
        time.sleep(1)


def start_data_reading(interface: Obd2Interface, read_duration=10):
    data_log = {pid_name: [] for pid_name in PIDS}
    start_time = time.time()

    while (time.time() - start_time) < read_duration:
        for pid_name, pid in PIDS.items():
            try:
                raw_response = interface.send_elm_command(pid.command)

                if raw_response and raw_response.startswith("41"):
                    value = interface.parse_pid_response(pid, raw_response)
                    print(f"{pid_name}: {value} {pid.unit}")
                    data_log[pid_name].append(value)
                else:
                    print(f"Falha ao ler {pid_name}. Resposta: '{raw_response}'")

            except ValueError as e:
                print(e)

        time.sleep(1)

    return data_log


def data_summary(data_log):
    for pid_name, values in data_log.items():
        if values:
            avg_value = sum(values) / len(values)
            print(f"Média de {pid_name}: {round(avg_value, 2)} {PIDS[pid_name].unit}")
        else:
            print(f"Nenhum dado coletado para {pid_name}.")


def main():
    config = Obd2Config()
    interface = Obd2Interface(config)

    start_interface(interface)

    print("\n--- Starting AT commands ---")
    start_at_commands(interface)

    print("\n--- Starting data reading ---")
    data_log = start_data_reading(interface, 20)

    print("\n--- Data collection summary ---")
    data_summary(data_log)

    stop_interface(interface)


if __name__ == "__main__":
    main()
