#! /usr/bin/python3

import os
import requests as req

endpoint = ""

def main():
        trustedIp = os.getenv("trusted_ip")
        bytesReceived = os.getenv("bytes_received")
        bytesSent = os.getenv("bytes_sent")
        cn = os.getenv("common_name")
        type = os.getenv("script_type")
        headers = { "Content-Type": "application/json", "Accept": "application/json" }
        body = { "type": type, "trusted_ip": trustedIp, "bytes_sent": bytesSent, "bytes_received": bytesReceived, "common_name" : cn }
        r = req.post(endpoint, headers=headers, json=body)
        result = r.json()
main()

os._exit(0)
