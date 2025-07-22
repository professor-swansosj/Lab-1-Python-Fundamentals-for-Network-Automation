# Network Automation Fundamentals Assignment

## :triangular_flag_on_post: Learning Goals

- Work with Python Functions, Classes, and Methods
- Impliment Exception and Error Handling
- Working with structured data [`JSON, YAML, XML, CSV`]


## :globe_with_meridians: Overview:

From a network automation perspective we leverage more advanced features in Python that will be covered in this lab.  Features like Functions(), Classes, Methods, and Modules help to break our code up to be more readable and easier to work on. As a Network Automation professional you will find that structured data is heavily utilized. There are different forms of structured data and here we will focus on the following; JSON, YAML, XML, and CSV. To provide context at where you may see some of these here are some scenarios which would require knowlege of each.

- Ansible = YAML (Used to write Ansible Playbooks)
- REST API Calls = JSON (Requests to Restful API Servers are written and results returned in JSON)
- NETCONF = XML (The NETCONF protocol uses XML to write it's requests and return results)
- INVENTORY = CSV (Many appliances and automation tools uses CSV files to pass in the inventory of devices)

### :wrench: Python Functions
Building off the Basics in Python from your Scripting course one of the most useful features of Python is the ability to write your own functions(). A `Python Function` is simply a block of code that you can reuse. Rather than write giant single execution programs we break the code up into smaller blocks that we call functions(). A function can take different inputs known as arguments such as variables, lists, dictionaires, and tuples as an input that will be passed to the function upon execution. Functions do not require arguments to be passed in but it is common to see. For example a simply function that prints a message does not need anything else to execute successfully where a custom message that would require say a device hostname as part of the message will need that hostname passed in upon runtime. 

### :package: Python Objects

A Python object is a defined Class where the attributes of the class help to define an object. For example if I define an object as `Class Switch:` I may include attributes such as hostname, vendor, IP, vlans, and STP Priority where a `Class Router:` would include attributes such as hostname, vendor, IP, routing protocol, and router-id. Additionally you can add Methods to your Classes which are simply functions that relate to the Class. So if I created a method for my Switch: Class I would create a method such as `def configure_access_port(interface)` or for my Router Class `def configure_static_route(route)`. Notice the methods are just fucntions about whatever they are specific to the Class Object. A switch switches packets on a layer 2 network and a router routes packets across a layer 3 network. 

### :rotating_light: Exceptions and Error Handling

There may be times where our code is going to fail.  When a block of code fails you recieve two things of importance 1) The traceback on where the failure occured in the code. 2) The Exception that was raised which can be translated to the error message. When a Exception is raised in Python it halts the execution of the code where it is and produces these two items. However, what if we don't want our entire program to fail based on a minor error? This is where Error Handling and Exceptions come in. Using Pythons built in `Try:...Except:` features you can gracefully handle the error and how you want the program to procede whether that be printing the error to a file, stopping the program, or do nothing and continue with the code execution.

### :page_facing_up: Logging

A note on the logging syntax you see here. It is usually a good idea to capture all your logs to a file and export to a central logging system. Although we are not going to go too deep on logging know it is a standard feature and procedure when writing your code to write the logs to a file. We are doing it here for a very important reason which is **THE LOGS WRITTEN TO THE LOG FILE IS WHAT IS USED TO DETERMINE YOUR GRADE!!!** If your script does not produce any logs to the log file the file will be blank and therefore you will not receive credit for your work. Under each instruction I will inform you where you are to insert a logging message so I know the program executed with all the requirements.

### JSON
JSON stands for Javascript Object Notation and is heavily adopted in the industry especially for programming against APIs. JSON is represented as key:value pairs and are structured the exact same as a Python Dictionary. Below is a JSON Object that containers two network devices and is represented by their IP and device type. 

```json
[
  {
    "hostname": "core-sw01",
    "ip": "192.168.1.1",
    "type": "Switch"
  },
  {
    "hostname": "edge-fw01",
    "ip": "192.168.1.254",
    "type": "Firewall"
  }
]
```

### YAML
YAML or YAML Ain't Markup Language is a component of JSON that is meant for better readability by Humans. It utilizes indentation to represent variables, lists, and dictionaireies. Since it is a compontent of JSON any valid YAML file is also a valid JSON file. Below is a YAML Object which contains a list of interfaces and their attributes.

```yaml
interfaces:
  - name: Gig0/1
    status: up
    vlan: 10
  - name: Gig0/2
    status: down
    vlan: 20
```

### XML
XML has been presented to network engineers for a long time already. The Cisco Nexus platform, Juniper, and Palo Alto all represent their configuration in XML. Heck the entire language of web pages `HTML` is XML. XML is not very human readable but great for machines to process. It uses the concept of tags<> and nested objects to represnt their informatoin. Every tag that is created must also be accompanied by a closing tag. Below we see some XML to represent a list of VLANS.

```xml
<vlans>
  <vlan>
    <id>10</id>
    <name>Users</name>
  </vlan>
  <vlan>
    <id>20</id>
    <name>Servers</name>
  </vlan>
</vlans>
```

### CSV
Finally CSV or Comma Separated Values is simply a list of items where the first line of the file represents the headers and each line represents a single objects attributes. Each attribute is separated by a comma as seen below.

```csv
hostname,location,role
core-sw01,DataCenter,Switch
edge-fw01,Branch,Firewall
```

---

## :card_file_box: File Structure:

It is important to start to understand the file structure for a given project. In python we break our Classes, Data, and Functions in separate files and import them as modules to their respective code base. This eventually leaves you with a simple few lines of code called the `main guard` that will kick off the script typically represented as `if __name__ == __main__: main()` which says if the system variable of `__name__` is equal to `__main__` which is true when the file being executed is referenced as the main file. In example if the file is named "script.py" and I run the command `python script.py` the system variable will set `__name__` equal to `__main__` and we declare our main() function in this file which references our other files on import. You will see examples of this throughout this course and is the standard in Python. 

```
network-automation-lab/
├── data/
│   ├── devices.json
│   ├── interfaces.yaml
│   ├── vlans.xml
│   └── inventory.csv
├── logs/
│   └── lab.log
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── parser_utils.py
│   └── network_device.py
├── tests/
│   └── test_lab.py
├── .github/
│   └── workflows/
│       └── autograding.yml
├── README.md
└── requirements.txt
```

---

## Components:

### 1. **Classes and Methods** (`network_device.py`)
Explanations are included below as Python comments with `#` which python will ignore when ran. These are simply notes from one developer to another. Multiline comments in python are annotated with ``` for both opening or closing the comment. 
```python
import logging #This is where we import the built in python logging module

class NetworkDevice: #Define our Class object of NetworkDevice
    def __init__(self, hostname, ip, device_type): #Initialize the object as well as the attributes
        self.hostname = hostname        #Define attribute hostname
        self.ip = ip                    #Define attribute ip 
        self.device_type = device_type  #Define attribute device_type

    def summarize(self):  #Defined a module for our NetworkDevice Class
        msg = f"{self.hostname} ({self.device_type}) - {self.ip}" #Creates a variable string dyanmically filled
        logging.info(f"DEVICE_SUMMARY: {msg}")                    #Generates a log message to include the output
        return msg        #Returns the output to the source code that called it
```

### 2. **Functions and Error Handling** (`parser_utils.py`)
```python
import json, yaml, xml.etree.ElementTree as ET, csv, logging

def parse_json(path):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
            logging.info(f"PARSE_JSON_SUCCESS: Loaded {len(data)} entries")
            return data
    except Exception as e:
        logging.error(f"PARSE_JSON_ERROR: {e}")
        return []

# Similar functions for YAML, XML, CSV
```

### 3. **Main Application** (`main.py`)
```python
import logging
from src.parser_utils import parse_json, parse_yaml, parse_xml, parse_csv
from src.network_device import NetworkDevice

logging.basicConfig(filename='logs/lab.log', level=logging.INFO)

def main():
    json_devices = parse_json('data/devices.json')
    for d in json_devices:
        dev = NetworkDevice(d['hostname'], d['ip'], d['type'])
        dev.summarize()

if __name__ == '__main__':
    main()
```

---

## ✅ Grading Points Breakdown (example)
- 2 pts: JSON parsed correctly (`PARSE_JSON_SUCCESS` in log)
- 2 pts: At least one device summarized (`DEVICE_SUMMARY` log)
- 2 pts: Error logged properly if missing file (`PARSE_JSON_ERROR`)
- 1 pt each: Similar logic for YAML, XML, and CSV parsing

---


