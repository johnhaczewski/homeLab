#!/usr/bin/env python
import json
import re
import sys
import time
import urllib2
from influxdb import InfluxDBClient
from datetime import datetime

wu_json = urllib2.urlopen('http://api.wunderground.com/api/***API_KEY***/conditions/q/PA/Hunlock_Creek.json')
json_string = wu_json.read()
parsed_json = json.loads(json_string)

temp_f = parsed_json['current_observation']['temp_f']
rel_hum = parsed_json['current_observation']['relative_humidity']
feeltemp_f = parsed_json['current_observation']['feelslike_f']
wind_mph = parsed_json['current_observation']['wind_mph']
precip_1hr_in = parsed_json['current_observation']['precip_1hr_in']
pressure_in = parsed_json['current_observation']['pressure_in']

rel_hum_val = re.match("(.*?)%", rel_hum)

time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
client = InfluxDBClient('localhost', 8086, 'User', 'Pass', 'DB')

json_body = [
    {
        "measurement": "weather",
        "time": time,
        "fields": {
            "temp_f": temp_f,
            "feeltemp_f": feeltemp_f,
            "rel_hum_val": rel_hum_val.group(1),
            "wind_mph": wind_mph,
            "precip_1hr_in": precip_1hr_in,
            "pressure_in": pressure_in
        }
    }
]

client.write_points(json_body)

wu_json.close()
