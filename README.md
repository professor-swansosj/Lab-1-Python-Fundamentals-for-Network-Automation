# Lab 1 — Python Fundamentals & Structured Data

**Course:** Software Defined Networking  
**Module:** Network Automation Fundamentals • **Lab #:** 1  
**Estimated Time:** 60–90 min

## Objectives
- Build and use Python functions, classes, and methods.
- Implement basic exception handling with try/except.
- Work with structured data files: JSON, YAML, XML, and CSV.
- Log meaningful events to a file for grading and troubleshooting.
- Organize code into modules and run via the main guard.

## Prerequisites
- Python 3.11 (via the provided dev container)
- Accounts: GitHub
- Devices/Sandboxes: Local filesystem + sample structured data

## Overview
This lab warms up core Python skills for network automation. You’ll separate logic into modules (class + parsing helpers), read structured data (JSON, YAML, XML, CSV), and emit clear log lines that double as your grading criteria.


## Resources
- [Python logging](https://docs.python.org/3/library/logging.html)- [json](https://docs.python.org/3/library/json.html)- [yaml (PyYAML)](https://pyyaml.org/wiki/PyYAMLDocumentation)- [xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html)- [csv](https://docs.python.org/3/library/csv.html)

## FAQ
**Q:** Where should logs go?  
**A:** Write to `logs/lab.log` and include the required markers listed in the README.

**Q:** Why split code into modules?  
**A:** It keeps functions/classes reusable and testing simpler; the main program stays small.



## Deliverables
- Standardized README describing objectives, prerequisites, grading, and tips.
- Step-by-step INSTRUCTIONS with required log markers; artifacts created under data/ and logs/.
- Grading: **75 points**

## Grading Breakdown
| Step | Requirement | Points |
|---|---|---|
| Step 2 | Dev Container opened; dependencies available | 5 |
| Step 4 | JSON parsed successfully (`PARSE_JSON_SUCCESS`) | 5 |
| Step 4 | YAML parsed successfully (`PARSE_YAML_SUCCESS`) | 5 |
| Step 4 | XML parsed successfully (`PARSE_XML_SUCCESS`) | 5 |
| Step 4 | CSV parsed successfully (`PARSE_CSV_SUCCESS`) | 5 |
| Step 5 | At least one device summarized (`DEVICE_SUMMARY`) | 5 |
| Step 6 | Interface message logged (`INTERFACE_MSG`) | 5 |
| Step 6 | Device message logged (`DEVICE_MSG`) | 5 |
| Step 6 | VLAN message logged (`VLAN_MSG`) | 5 |
| Step 7 | Clean module structure (class + parser functions imported and used) | 10 |
| Step 8 | Commit, push, and PR opened; logs present with start/end markers | 15 |
| **Total** |  | **75** |

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



## Autograder Notes
- Log file: `logs/lab.log`
- Required markers: `LAB1_START`, `[STEP 2] Dev Container Started`, `PARSE_JSON_SUCCESS`, `PARSE_YAML_SUCCESS`, `PARSE_XML_SUCCESS`, `PARSE_CSV_SUCCESS`, `DEVICE_SUMMARY`, `INTERFACE_MSG`, `DEVICE_MSG`, `VLAN_MSG`, `LAB1_END`

## License
© 2025 Your Name — Classroom use.

# HAPPY CODING!

**Sincerely, Professor Swanson**