"""RegExp: write a script that parses "ifconfig" output using the "re" module and prints the MAC & IP addresses of the main network interface. It's preferred to use a single regular expression.
"""

import subprocess
from re import DOTALL, search


def get_main_interface():
    """Get the main interface using route command"""
    try:
        route_main = subprocess.check_output(["route", "-n", "get", "default"]).decode()
        print(route_main)
        main_in = search(r"interface: (\w+)", route_main)
        print(main_in)
        print(main_in.group(1))
        return main_in.group(1)
    except subprocess.CalledProcessError as e:
        print(f"Error executing route command: {e}")


def get_network_info(interface):
    try:
        config_output = subprocess.check_output(["ifconfig"]).decode()
        # print(config_output)
        print(type(config_output))
    except FileNotFoundError:
        print("ifconfig command not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing ifconfig command: {e}")

    # Method number one with direct name into regex

    mac_pattern = r"en0:.*?\n\s*ether\s+([0-9a-fA-F:]{17})"
    mac_match = search(mac_pattern, config_output, DOTALL)

    ip_pattern = r"en0:.*?\n\s*inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    ip_match = search(ip_pattern, config_output, DOTALL)

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

    # Method with interface name as variable

    mac_pattern = r"{0}:.*?\n.*?ether\s+([0-9a-fA-F:]{{17}})".format(interface)
    mac_match = search(mac_pattern, config_output, DOTALL)
    if mac_match:
        mac_address = mac_match.group(1)
        print(f"MAC Address: {mac_address}")
    else:
        print("MAC address not found")

    ip_pattern = (
        r"{0}:.*?\n.*?inet\s+(\d{{1,3}}\.\d{{1,3}}\.\d{{1,3}}\.\d{{1,3}})".format(
            interface
        )
    )
    ip_match = search(ip_pattern, config_output, DOTALL)

    if ip_match:
        ip_address = ip_match.group(1)
        print(f"IP Address: {ip_address}")
    else:
        print("IP address not found")


if __name__ == "__main__":
    get_network_info(get_main_interface())
