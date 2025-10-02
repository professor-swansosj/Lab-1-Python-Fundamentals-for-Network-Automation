# Lab 1 — Advanced Python for Network Automation

**Course:** Software Defined Networking  
**Module:** Advanced Python for Network Automation • **Lab #:** 1  
**Estimated Time:** 60–90 min

## Repository structure

```text
target
├── .devcontainer
│   └── devcontainer.json
├── .gitignore
├── .markdownlint.json
├── .markdownlintignore
├── .pettierrc.yml
├── INSTRUCTIONS.backup.md
├── INSTRUCTIONS.md
├── README.backup.md
├── README.md
├── data
│   ├── devices.json
│   ├── interfaces.yaml
│   ├── inventory.csv
│   └── vlans.xml
├── lab.yml
├── prettierrc.yml
├── requirements.txt
└── src
    ├── __init__.py
    ├── main.py
    ├── network_device.py
    └── parser_utils.py
```


## Lab Topics

### Python Functions
Building off the Basics in Python from your Scripting course one of the most useful features  of Python is the ability to write your own functions(). A `Python Function` is simply a block  of code that you can reuse. Rather than write giant single execution programs we break the code  up into smaller blocks that we call functions(). A function can take different inputs known as  arguments such as variables, lists, dictionaires, and tuples as an input that will be passed to  the function upon execution. Functions do not require arguments to be passed in but it is common  to see. For example a simply function that prints a message does not need anything else to execute  successfully where a custom message that would require say a device hostname as part of the message  will need that hostname passed in upon runtime.
A python function is a block of code that can be called after it is defined. As a best practice you  typically want to break up as much of your code as possible into mutliple functions. As a genneral  guidline you should aim to have your functions be no longer than 20-30 lines of code. Most of the time  you will need to pass information into your function so it can perform some type of logic on the data.  In the function below we pass a argument name to the function and then print a message using that name.


```python
def greeting(name): #Define a function called greeting that takes one argument name
    print(f"Hello, {name}!") #Print a message using the name argument

name = "Sheldon" #Define a variable name

greeting(name) #Call the function greeting and pass in the variable name

```

### Python Classes/Objects
Another powerful feature of Python is the ability to create your own `Classes` and `Objects`.  A class is a blueprint for an object. An object is an instance of a class. Classes can contain  attributes (variables) and methods (functions). Classes are used to model real-world entities  and their behaviors. For example, you might have a class called `NetworkDevice` that has attributes  like `hostname`, `ip_address`, and `device_type`, and methods like `connect()`, `disconnect()`,  and `get_status()`. You can then create multiple instances of the `NetworkDevice` class, each  representing a different network device.
In python we define objects by defining the class. Think of an object as a way to represent anything  in the real world. The attributes help to describe the object. Inside an object we can also define  methods which are functions that are related to our object.


```python
class NetworkDevice: #Define our Class object of NetworkDevice
  def __init__(self, hostname, ip, device_type): #Initialize the object as well as the attributes
      self.hostname = hostname        #Define attribute hostname
      self.ip = ip                    #Define attribute ip 
      self.device_type = device_type  #Define attribute device_type
      self.vendor = "Cisco"           #Define attribute vendor with a default value of Cisco

  def summarize(self): #Define a method called summarize
      return f"{self.hostname} ({self.device_type}) - {self.ip}" #Return a summary string

device1 = NetworkDevice("router1", "192.168.1.1", "router") #Create an instance of the NetworkDevice class
print(device1.summarize()) #Call the summarize method on the device1 object

```

### Exceptions and Error Handling
When writing code, it is common to encounter errors. Python provides a way to handle these errors  gracefully using `try` and `except` blocks. The code that might raise an exception is placed inside  the `try` block, and the code that handles the exception is placed inside the `except` block. This  allows you to catch and handle specific exceptions, preventing your program from crashing. For example,  when working with files, you might want to catch a `FileNotFoundError` if the file you are trying to  open does not exist.
You will notice in this function the use of the syntax `try:` and `except` which is a python feature that  allows you to gracefully handle errors in your code without it crashing the entire program. In our example  below we define the variable name with a integer value of 25 not a string. The function starts with the `try:`  statement essentially saying "Try to perform this block of code which would print a message to the terminal as a string. Problem is you can't concatenate a string and an integer so the code will raise a `TypeError` exception. The `except` statement will catch the `TypeError` exception and assign it to the variable e. We can then print the error message to the terminal. Meanwhile our code keeps executing without crashing the entire program.


```python

name = 25

try:
    print(f"Hello, {name}!")  #This will raise an error because name is not a string
except TypeError as e:        #Catch the TypeError exception and assign it to variable e
    print(f"Error: {e}")      #Print the error message

```

### JSON
`JSON` (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans  to read and write, and easy for machines to parse and generate. It is commonly used for transmitting  data between a server and a web application, as well as for configuration files. In Python, you can  work with JSON data using the built-in `json` module, which provides methods for parsing JSON strings  into Python objects (like dictionaries and lists) and for converting Python objects back into JSON strings.


```json
[
  {
    "hostname": "router1",
    "ip_address": "192.168.1.1",
    "device_type": "router"
  },
  {
    "hostname": "switch1",
    "ip_address": "192.168.1.2",
    "device_type": "switch"
  }
]

```

### YAML
`YAML` (YAML Ain't Markup Language) is a human-readable data serialization format that is often used for  configuration files and data exchange between languages with different data structures. In Python, you  can work with YAML data using the `PyYAML` library, which provides methods for parsing YAML strings into  Python objects and for converting Python objects back into YAML strings.


```yaml
interfaces:
  - name: GigabitEthernet0/1
    status: up
    description: Uplink to ISP
  - name: GigabitEthernet0/2
    status: down
    description: Spare port

```

### XML
`XML` (eXtensible Markup Language) is a markup language that defines a set of rules for encoding documents in a format  that is both human-readable and machine-readable. It is commonly used for data exchange between different systems and  applications. In Python, you can work with XML data using the built-in `xml.etree.ElementTree` module, which provides  methods for parsing XML strings into Python objects and for converting Python objects back into XML strings.


```xml
<devices>
  <device>
    <hostname>router1</hostname>
    <ip_address>192.168.1.1</ip_address>
    <device_type>router</device_type>
  </device>
  <device>
    <hostname>switch1</hostname>
    <ip_address>192.168.1.2</ip_address>
    <device_type>switch</device_type>
  </device>
</devices>

```

### CSV
`CSV` (Comma-Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database. Each  line in a CSV file represents a row of data, and each value in the row is separated by a comma. In Python, you can work with  CSV data using the built-in `csv` module, which provides methods for reading and writing CSV files.


```csv
hostname,ip_address,device_type
router1,192.168.1.1,router
switch1,192.168.1.2,switch

```


## 🔧 Troubleshooting & Pro Tips
**Dev container / dependencies**  
*Symptom:* ImportError for yaml, csv, or XML libraries  
*Fix:* Reopen in dev container; verify with `pip list`. If needed, run `pip install -r requirements.txt`.

**Wrong data paths**  
*Symptom:* FileNotFoundError when parsing `data/*`  
*Fix:* Run from repo root and use relative paths like `data/devices.json`.

**Empty or invalid JSON/YAML/XML**  
*Symptom:* Parse errors or zero-length data  
*Fix:* Use the provided sample files; validate formatting before parsing.

**No logs written**  
*Symptom:* `logs/lab.log` missing or empty  
*Fix:* Call `logging.basicConfig(filename='logs/lab.log', level=logging.INFO)` once, near program start.


## License
© 2025 Sheldon Swanson — Classroom use.
