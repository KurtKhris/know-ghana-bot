import requests
import json


response = requests.get("http://ghdata.herokuapp.com/regions/")

print(response.status_code) #200

#print(response.json())

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#jprint(response.json())

data = response.json()['data']
#jprint(data)
regions = []

for d in data:
    
    reg = d['name']
    regions.append(reg)

print(regions)

