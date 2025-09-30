# Instructions — Lab 1 — Python Fundamentals & Structured Data

> **Before you begin:** Open the dev container, confirm Python runs, and ensure you can list files under `data/` and write to `logs/`.


Follow these steps in order.

> **Logging Requirement:** Write progress to `logs/lab.log` as you complete each step.

## Step 1 — Clone the Repository
**Goal:** Get the starter locally.

**What to do:**  
Clone your Classroom repo and `cd` into it. Review the provided `data/` files and `src/` layout.


**You’re done when:**  
- You are in the repo folder and see `data/`, `logs/`, and `src/`.
- You created `logs/` if it didn’t exist.


**Log marker to add:**  
`[LAB1_START]`

## Step 2 — Open Dev Container
**Goal:** Use the standardized toolchain.

**What to do:**  
Reopen in container and wait for the first-time install to finish. Verify `python --version`.


**You’re done when:**  
- Python prints a version (3.11+).
- You append `[STEP 2] Dev Container Started` to the log.


**Log marker to add:**  
`[[STEP 2] Dev Container Started]`

## Step 3 — Implement `NetworkDevice` class
**Goal:** Model a network device and log a summary.

**What to do:**  
In `src/network_device.py`, implement/confirm the `NetworkDevice` class with `summarize()`
that logs `DEVICE_SUMMARY: <hostname> (<type>) - <ip>`.


**You’re done when:**  
- A call to `summarize()` returns a string and writes a `DEVICE_SUMMARY` line to the log.


**Log marker to add:**  
`[DEVICE_SUMMARY]`

## Step 4 — Implement parser helpers
**Goal:** Parse each structured data file safely.

**What to do:**  
In `src/parser_utils.py`, implement `parse_json()`, `parse_yaml()`, `parse_xml()`, and `parse_csv()`.
On success, log `PARSE_*_SUCCESS`; on failure, log `PARSE_*_ERROR` and return an empty list.


**You’re done when:**  
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


**You’re done when:**  
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


**You’re done when:**  
- Terminal shows the three message types at least once.
- Log file includes `INTERFACE_MSG`, `DEVICE_MSG`, and `VLAN_MSG`.


**Log marker to add:**  
`[INTERFACE_MSG, DEVICE_MSG, VLAN_MSG]`

## Step 7 — Refactor & tidy
**Goal:** Keep modules clean and imports explicit.

**What to do:**  
Ensure only `main.py` runs the workflow; helpers stay importable and short.


**You’re done when:**  
- Code style is clean; modules are < ~100 lines each.


**Log marker to add:**  
`[MODULES_OK]`

## Step 8 — Commit, push, and open PR
**Goal:** Submit work for grading.

**What to do:**  
Commit your changes; push; open a PR targeting `main`.


**You’re done when:**  
- PR is open and CI passes.


**Log marker to add:**  
`[LAB1_END]`


## Submission Checklist
- [ ] `logs/lab.log` exists and includes LAB1_START/LAB1_END and all required markers.
- [ ] Parser functions handle JSON, YAML, XML, and CSV without crashing.
- [ ] At least one `DEVICE_SUMMARY` log line appears.
- [ ] `INTERFACE_MSG`, `DEVICE_MSG`, and `VLAN_MSG` appear at least once each.
- [ ] All code lives under `src/` and runs from `main.py`.
