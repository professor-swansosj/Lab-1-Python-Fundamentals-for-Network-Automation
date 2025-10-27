# Lab 1 — Advanced Python for Network Automation

**Course:** Software Defined Networking  
**Module:** Advanced Python for Network Automation • **Lab #:** 1  
**Estimated Time:** 60–90 min

## Repository structure

```text
Lab-1-Python-Fundamentals-for-Network-Automation
├── .devcontainer
│   └── devcontainer.json
├── .gitignore
├── .markdownlint.json
├── .markdownlintignore
├── .pettierrc.yml
├── INSTRUCTIONS.backup.md
├── INSTRUCTIONS.md
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

- Python Functions
- Python Classes/Objects
- Exceptions and Error Handling
- JSON
- YAML
- XML
- CSV
- Working with Files
- Importing Modules

## Grading

Your labs will be automatically graded when you upload the completed lab to GitHub Classroom. Your script will be
checked for guarenteed lines of code that must be there as they are predefined and/or built in syntax for either
python or the module you have to use to complete the Lab.

### Logging

You will need to impliment logging in your code with specific log messages after certain tasks have been completed.
Logging for a modular program such as our labs requires import and configuration in the main entrypoint of your code.
In the main entry point you must import logging and set the base config. This code snippet is provided for you below.

```python
# For the main entry point
import loggging

logging.basicConfig(filename='logs/lab.log', level=logging.INFO)
```

For any other modules that will be using in your code you can simply import the logging module and it will reference the
config that was defined in the main entry point. i.e.

```python
import loggging
```

To log specific message simply write a line as an info log along with the message your directed to log.

```python
import loggging

def some_function()
  msg = "Some Message"
  print(msg)
  logging.info(f"LOG STRING: {msg}")
```

### IMPORTANT

**IF YOU LOG FILE DOESN'T HAVE THE CORRECT MESSAGE IT DID NOT HAPPEN! CODING REQUIRES CAREFUL ATTENTION TO DETAIL. IT IS**
**EXPECTED OF YOU AT A SENIOR LEVEL TO BE ATTENTIVE TO WHAT YOU SUBMIT.**

## DO NOT ALTER

- Anything in the .devcontainer directory or your devcontainer won't work and will negatively effect your grade
- Anyting in the .github directory **(AUTOMATIC GRADE OF 0 IF ANYTHING IN THIS DIRECTORY IS ALTERED)**
- The .markdownlint.json file
- The .markdownlintignore file

Any other files will altered will result in abnormal behavior of the lab. If you feel you have altered it beyond repair
simply clone another fresh copy.

## License

© 2025 Sheldon Swanson — Classroom use.
