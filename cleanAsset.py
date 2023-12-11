from pip._vendor import requests
import json
import re

API_KEY = 'REDACTED'
USER_AGENT = 'REDACTED'
URL = 'REDACTED'
COMPANY_DOMAIN = 'REDACTED'
UID = 'REDACTED'

headers = {
    'user-agent': USER_AGENT,
    'Authorization': f'Bearer {API_KEY}'
}

response = requests.get(f'{URL}Asset/{UID}', headers=headers)
json_data = response.json()
attributes = json_data.get('attributes')
cpu_pattern = r'Intel\(R\) Core\(TM\) (\S+)'
battery_pattern = r'\d+%'

#check for attribute list, if attributes are and CPU are found, set cpu_type variable
if attributes:
    for attribute in attributes:
        if attribute.get('typeName') == 'Battery Wear Level':
            battery_wear = attribute.get('value')
            battery_attr = attribute
        if attribute.get('typeName') == 'CPU Type':
            cpu_type = attribute.get('value')
            cpu_attr = attribute
            break

#convert/print function for json debugging
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def corrections(uid):
    #payload ship/post for specified UID/asset
    def ship_payload(data):
        response = requests.put(f'{URL}Asset/{UID}', headers=headers, json=data)
        if response.status_code == 200:
            print('Asset updated successfully!')
        else:
            print(f'PUT request failed with code {response.status_code}.')

    #"clean"/simplify Intel-based CPUs
    def clean_up_cpu(model):
        match = re.search(cpu_pattern, model)
        if match:
            print("Reformatting CPU.")
            return match.group(1)
        else:
            print("CPU already cleaned/no matching CPU criteria found.")
            return None
    
    def clean_battery(wear):
        match = re.search(battery_pattern, wear)
        if match:
            print('Battery wear already correctly formatted.')
            return None
        else:
            print('Reformatting battery wear.')
            return f'{wear}%'

    #check for formatting on battery and CPU
    cleaned_cpu = clean_up_cpu(cpu_type)
    cleaned_battery = clean_battery(battery_wear)
    if cleaned_cpu:
        cpu_attr['value'] = cleaned_cpu
    if cleaned_battery:
        battery_attr['value'] = cleaned_battery

    #ship payload once all operations are done
    payload = {'attributes': attributes}
    ship_payload(payload)

#run all corrections on specified UID
corrections(UID)
