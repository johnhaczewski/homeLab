#!/usr/bin/env python
import re
import sys
import time
from influxdb import InfluxDBClient
from datetime import datetime

t = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

lines = open('/var/log/speedtests/wan_speedtests.log').read().splitlines()
p = re.match("Ping: (.*?) ms", lines[0])
d = re.match("Download: (.*?) Mbit/s", lines[1])
u = re.match("Upload: (.*?) Mbit/s", lines[2])

client = InfluxDBClient('localhost', 8086, 'User', 'Pass', 'DB')

json_body = [
    {
        "measurement": "bandwidth",
        "time": t,
        "fields": {
            "ping": p.group(1),
            "dl": d.group(1),
            "ul": u.group(1)
        }
    }
]

client.write_points(json_body)
