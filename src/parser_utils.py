import json, yaml, csv, logging
import xml.etree.ElementTree as ET

def parse_json(path):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
            logging.info(f"PARSE_JSON_SUCCESS: Loaded {len(data)} entries")
            return data
    except Exception as e:
        logging.error(f"PARSE_JSON_ERROR: {e}")
        return []

def parse_yaml(path):
    try:
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
            logging.info(f"PARSE_YAML_SUCCESS: {len(data['interfaces'])} interfaces parsed")
            return data
    except Exception as e:
        logging.error(f"PARSE_YAML_ERROR: {e}")
        return {}

def parse_xml(path):
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        vlan_list = [(v.find('id').text, v.find('name').text) for v in root.findall('vlan')]
        logging.info(f"PARSE_XML_SUCCESS: {len(vlan_list)} VLANs parsed")
        return vlan_list
    except Exception as e:
        logging.error(f"PARSE_XML_ERROR: {e}")
        return []

def parse_csv(path):
    try:
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
            logging.info(f"PARSE_CSV_SUCCESS: {len(data)} inventory entries parsed")
            return data
    except Exception as e:
        logging.error(f"PARSE_CSV_ERROR: {e}")
        return []