"""RegExp: write a script that parses "ifconfig" output using the "re" module and prints the MAC & IP addresses of the main network interface. It's preferred to use a single regular expression.
JSON & YAML: given two files, devices.yaml & lab_envs.json, parse and combine them into one YAML file, which has "lab_env" attribute filled for each device. If there is no such env in the lab_envs.json, set it for the corresponding device to None."""
from re import search, DOTALL, IGNORECASE
import subprocess

def get_main_interface():
    """Get the main interface using route command"""
    try:
        route_main = subprocess.check_output(['route', '-n', 'get', 'default']).decode()
        print(route_main)
        main_if = search(r'interface: (\w+)', route_main)
        print(main_if.group(1))
        return main_if.group(1)
    except subprocess.CalledProcessError as e:
        print(f"Error executing route command: {e}")


def get_network_info(interface):
    try:
        config_output = subprocess.check_output(['ifconfig']).decode()
        print(config_output)
        print(type(config_output))
    except FileNotFoundError:
        print("ifconfig command not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing ifconfig command: {e}")

    pattern = rf'{interface}[\s\S]*?ether\s+([0-9a-fA-F:]{17})\s+.*?inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

    match = search(pattern, config_output)
    print(match)
    if match:
        mac_address = match.group(1)
        ip_address = match.group(2)
        print(f"MAC Address: {mac_address}")
        print(f"IP Address: {ip_address}")
    else:
        print('MAC and IP are not found')

    mac_pattern = rf'{interface}[\s\S]*?\n\s*ether\s+([0-9a-fA-F:]{17})'
    ip_pattern = rf'{interface}[\s\S]*?\n\s*inet\s+(\d{1, 3}\.\d{1, 3}\.\d{1, 3}\.\d{1, 3})'

    mac_match = search(mac_pattern, config_output)
    ip_match = search(ip_pattern, config_output)
    if mac_match:
        mac_address = mac_match.group(1)
        print(f"MAC Address: {mac_address}")
    else:
        print("MAC address not found")

    if ip_match:
        ip_address = ip_match.group(1)
        print(f"IP Address: {ip_address}")
    else:
        print("IP address not found")


if __name__ == "__main__":
    get_network_info(get_main_interface())