# Step 3 — Implement NetworkDevice class

import logging

# class named NetworkDevice with attributes
class NetworkDevice:
    def __init__(self, hostname, ip, type):
        self.hostname = hostname
        self.ip = ip
        self.type = type

# method named summarize that logs and prints device summary
    def summarize(self):
        msg = f"[DEVICE_SUMMARY]: {self.hostname} ({self.type}) - {self.ip}"

        print(msg)

        logging.info(msg)        
        return msg