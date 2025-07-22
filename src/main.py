import logging
from src.parser_utils import parse_json, parse_yaml, parse_xml, parse_csv
from src.network_device import NetworkDevice

logging.basicConfig(filename='logs/lab.log', level=logging.INFO)

def main():
    devices = parse_json('data/devices.json')
    for d in devices:
        dev = NetworkDevice(d['hostname'], d['ip'], d['type'])
        dev.summarize()

    parse_yaml('data/interfaces.yaml')
    parse_xml('data/vlans.xml')
    parse_csv('data/inventory.csv')

if __name__ == '__main__':
    main()