#!/usr/bin/env python3.6

import os
import requests
import sys
import json

from argparse import ArgumentParser

parser = ArgumentParser(description='Get the current weather information')
parser.add_argument('zip', help='zip/postal code to get the weather for')
parser.add_argument('--country', default='in', help='country zip/postal belongs to, default is "us"')

args = parser.parse_args()

#  We need to export OWM_API_KEY="24b5862a3f90e13e413196165f37b02e"

api_key = os.getenv('OWM_API_KEY')

if not api_key:
    print("Error: no 'OWM_API_KEY' provided")
    sys.exit(1)

url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&units=metric&appid={api_key}"

res = requests.get(url)

if res.status_code != 200:
    print(f"Error talking to weather provider: {res.status_code}")
    sys.exit(1)

weatherdata = json.loads(res.text)

print("Name : "+weatherdata['name']+'/'+weatherdata['sys']['country'])
print("Weather - "+weatherdata['weather'][0]['description'])
print("Temperature - "+str(weatherdata['main']['temp']))
