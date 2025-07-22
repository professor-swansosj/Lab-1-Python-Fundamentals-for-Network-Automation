import logging

class NetworkDevice:
    def __init__(self, hostname, ip, device_type):
        self.hostname = hostname
        self.ip = ip
        self.device_type = device_type

    def summarize(self):
        msg = f"{self.hostname} ({self.device_type}) - {self.ip}"
        logging.info(f"DEVICE_SUMMARY: {msg}")
        return msg