# Instructions — Lab 1 — Advanced Python for Network Automation

## Objectives
- Build and use Python functions, classes, and methods.
- Implement basic exception handling with `try/except`.
- Work with structured data formats: JSON, YAML, XML, and CSV.
- Write logs to file for testing and autograding.
- Organize code into modules and run via `main()` guard.

## Prerequisites
- Python 3.11 (via the provided dev container)
- Accounts: GitHub
- Devices/Sandboxes: Local filesystem + sample structured data
- Technical: - Basic Python syntax (variables, loops, conditionals).
- Familiarity with JSON, YAML, XML, and CSV formats.
- Git and GitHub basics (clone, commit, push, PR).
- Working with Files in Python.
- Basic logging in Python.
- VS Code and Dev Containers (or local Python setup).

## Overview
This first lab warms up your Python automation muscles. You'll refactor simple scripts into structured, reusable modules with functions, classes, and exception handling. You'll parse structured data (JSON, YAML, XML, CSV), write logs with the logging module, and output graded markers for autograding. Each function and class should reside in its own file inside `src/`. By the end, you'll have a clean, modular script that logs events for testing and serves as your foundation for later automation projects.


> **Before you begin:** Open the dev container, confirm Python runs, and ensure you can list files under `data/` and write to `logs/`.


## Resources
- [Python logging](https://docs.python.org/3/library/logging.html)- [json](https://docs.python.org/3/library/json.html)- [yaml (PyYAML)](https://pyyaml.org/wiki/PyYAMLDocumentation)- [xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html)- [csv](https://docs.python.org/3/library/csv.html)- [Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
## Deliverables
- `src/` contains: `main.py`, `parser_utils.py`, `network_device.py`.
- `logs/lab.log` contains required markers and log lines.
- Data files under `data/` (JSON, YAML, XML, CSV) successfully parsed.
- Pull request open to main branch with all artifacts committed.
- Grading: **75 points**

Follow these steps in order.

> **Logging Requirement:** Write progress to `logs/lab.log` as you complete each step.

## Step 1 — Clone the Repository
**Goal:** Get the starter locally.

**What to do:**  
Clone your Classroom repo and `cd` into it. Review the provided `data/` files and `src/` layout.


**You're done when:**  
- You are in the repo folder and see `data/`, `logs/`, and `src/`.
- You created `logs/` if it didn’t exist.


**Log marker to add:**  
`[LAB1_START]`

## Step 2 — Open Dev Container
**Goal:** Use the standardized toolchain.

**What to do:**  
Reopen in container and wait for the first-time install to finish. Verify `python --version`.


**You're done when:**  
- Python prints a version (3.11+).
- You append `[STEP 2] Dev Container Started` to the log.


**Log marker to add:**  
`[[STEP 2] Dev Container Started]`

## Step 3 — Implement `NetworkDevice` class
**Goal:** Model a network device and log a summary.

**What to do:**  
In `src/network_device.py`, implement/confirm the `NetworkDevice` class with `summarize()`
that logs `DEVICE_SUMMARY: <hostname> (<type>) - <ip>`.


**You're done when:**  
- A call to `summarize()` returns a string and writes a `DEVICE_SUMMARY` line to the log.


**Log marker to add:**  
`[DEVICE_SUMMARY]`

## Step 4 — Implement parser helpers
**Goal:** Parse each structured data file safely.

**What to do:**  
In `src/parser_utils.py`, implement `parse_json()`, `parse_yaml()`, `parse_xml()`, and `parse_csv()`.
On success, log `PARSE_*_SUCCESS`; on failure, log `PARSE_*_ERROR` and return an empty list.


**You're done when:**  
- Running the script produces `PARSE_JSON_SUCCESS`, `PARSE_YAML_SUCCESS`,
  `PARSE_XML_SUCCESS`, and `PARSE_CSV_SUCCESS` in the log.


**Log marker to add:**  
`[PARSE_JSON_SUCCESS, PARSE_YAML_SUCCESS, PARSE_XML_SUCCESS, PARSE_CSV_SUCCESS]`

## Step 5 — Wire up `main.py`
**Goal:** Load data, build objects, and summarize.

**What to do:**  
In `src/main.py`, configure logging to `logs/lab.log` once.
Load `data/devices.json` (and other files) using your parser helpers.
For each device, build a `NetworkDevice` and call `summarize()`.


**You're done when:**  
- Device summaries are printed and logged.


**Log marker to add:**  
`[DEVICE_SUMMARY]`

## Step 6 — Print + log required messages
**Goal:** Echo required lines for grading.

**What to do:**  
Iterate your parsed data to produce:
  - `Interface { interface.name } is { interface.status }`
  - `Device { device.hostname } is a { device.location } { device.role }`
  - `VLAN { vlan.id } is the { vlan.name }`
After each print, log:
  - `logging.info(f"INTERFACE_MSG: {msg}")`
  - `logging.info(f"DEVICE_MSG: {msg}")`
  - `logging.info(f"VLAN_MSG: {msg}")`


**You're done when:**  
- Terminal shows the three message types at least once.
- Log file includes `INTERFACE_MSG`, `DEVICE_MSG`, and `VLAN_MSG`.


**Log marker to add:**  
`[INTERFACE_MSG, DEVICE_MSG, VLAN_MSG]`

## Step 7 — Refactor & tidy
**Goal:** Keep modules clean and imports explicit.

**What to do:**  
Ensure only `main.py` runs the workflow; helpers stay importable and short.


**You're done when:**  
- Code style is clean; modules are < ~100 lines each.


**Log marker to add:**  
`[MODULES_OK]`

## Step 8 — Commit, push, and open PR
**Goal:** Submit work for grading.

**What to do:**  
Commit your changes; push; open a PR targeting `main`.


**You're done when:**  
- PR is open and CI passes.


**Log marker to add:**  
`[LAB1_END]`


## FAQ
**Q:** Where should logs go?  
**A:** Write to `logs/lab.log` and include the required markers listed in the README.

**Q:** Why split code into modules?  
**A:** It keeps functions/classes reusable and testing simpler; the main program stays small.


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

## Autograder Notes
- Log file: `logs/lab.log`
- Required markers: `LAB1_START`, `[STEP 2] Dev Container Started`, `PARSE_JSON_SUCCESS`, `PARSE_YAML_SUCCESS`, `PARSE_XML_SUCCESS`, `PARSE_CSV_SUCCESS`, `DEVICE_SUMMARY`, `INTERFACE_MSG`, `DEVICE_MSG`, `VLAN_MSG`, `LAB1_END`

## Submission Checklist
- [ ] `logs/lab.log` exists and includes LAB1_START/LAB1_END and all required markers.
- [ ] Parser functions handle JSON, YAML, XML, and CSV without crashing.
- [ ] At least one `DEVICE_SUMMARY` log line appears.
- [ ] `INTERFACE_MSG`, `DEVICE_MSG`, and `VLAN_MSG` appear at least once each.
- [ ] All code lives under `src/` and runs from `main.py`.
