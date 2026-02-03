import json
import yaml
import csv
import logging
import xml.etree.ElementTree as ET


# Parse a JSON file
def parse_json(path):    
    try:
        with open(path, "r") as f:
            data = json.load(f)
        
        logging.info("PARSE_JSON_SUCCESS")
        return data
    
    except (FileNotFoundError, json.JSONDecodeError):
        logging.error("PARSE_JSON_ERROR")
        return []


#Parse a YAML file
#Extra space before def had me stuck here   
def parse_yaml(path):

    try:
        with open(path, "r") as f:
            data = yaml.safe_load(f)

        logging.info("PARSE_YAML_SUCCESS")
        return data

    except (FileNotFoundError, yaml.YAMLError):
        logging.error("PARSE_YAML_ERROR")
        return []   


#Parse an CSV file
def parse_csv(path):
    
    try:
        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            data = list(reader)

        logging.info("PARSE_CSV_SUCCESS")
        return data

    except (FileNotFoundError, csv.Error):
        logging.error("PARSE_CSV_ERROR")
        return []


# Parse an XML file
def parse_xml(path):

    try:
        tree = ET.parse(path)
        root = tree.getroot()
        
        data = []
        for vlan in root.findall("vlan"):
            data.append({
                "id": vlan.findtext("id"),
                "name": vlan.findtext("name")
            })
            
        logging.info("PARSE_XML_SUCCESS")
        return data

    except (FileNotFoundError, ET.ParseError):
        logging.error("PARSE_XML_ERROR")
        return []
