import logging
from pathlib import Path


from src.parser_utils import (
    parse_json,
    parse_yaml,
    parse_csv,
    parse_xml
)
from src.network_device import NetworkDevice


def main():
    
    devices = parse_json("data/devices.json")
    interfaces = parse_yaml("data/interfaces.yaml")
    inventory = parse_csv("data/inventory.csv")
    vlans = parse_xml("data/vlans.xml")

    
    for device in devices:
        network_device = NetworkDevice(
            device.get("hostname"),
            device.get("ip"),
            device.get("type")
        )
        network_device.summarize()


    # interfaces: INTERFACE_MSG
    if isinstance(interfaces, dict):
        interfaces = interfaces.get("interfaces", [])

    for interface in interfaces:
        name = interface.get("name")
        status = interface.get("status")

        if name and status:
            msg = f"Interface {name} is {status}"
            print(msg)
            logging.info(f"INTERFACE_MSG: {msg}")


    # inventory: DEVICE_MSG
    for device in inventory:
        hostname = device.get("hostname")
        location = device.get("location")
        role = device.get("role")

        if hostname and location and role:
            msg = f"Device {hostname} is a {location} {role}"
            print(msg)
            logging.info(f"DEVICE_MSG: {msg}")


    # vlans: VLAN_MSG
    for vlan in vlans:
        id = vlan.get("id")
        name = vlan.get("name")

        if id and name:
            msg = f"VLAN {id} is the {name}"
            print(msg)
            logging.info(f"VLAN_MSG: {msg}")


if __name__ == "__main__":
    Path("logs").mkdir(exist_ok=True)

    #configure logging to logs/lab.log once
    logging.basicConfig(
        filename="logs/lab.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s"
    )

    # Log Marker
    logging.info("[LAB1-START]")
    main()
    logging.info("[LAB1-END]")
