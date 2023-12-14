#JWT info redacted, main function only
#Main
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
def main():
    #Initial server prod for asset data
    response = requests.get(f'{URL}Asset/{UID}', headers=headers)
    if response.status_code != 200:
        print(f'ERROR: Server responded with code {response.status_code}')
        exit()
    #Data retrieved from successful server response
    json_data = response.json()
    attributes = json_data.get('attributes')
    #Dictionary of attributes to search for (pulled from Razor)
    attribute_dict = {
        'CPU Type': None,
        'Battery Wear Level': None
    }
    if attributes:
        for attribute in attributes:
            typeName = attribute.get('typeName')
            if typeName in attribute_dict:
                attribute_dict[typeName] = attribute.get('value')
    if all(value is None for value in attribute_dict.values()):
        print('Attributes not found! Invalid UID? Exiting...')
        exit()


    #Preload variables
    cpu_pattern = r'(Intel\(R\)) (\S+) (\S+)'
    battery_pattern = r'\d+%'


    #payload ship/post for specified UID/asset
    def ship_payload(data):
        response = requests.put(f'{URL}Asset/{UID}', headers=headers, json=data)
        if response.status_code == 200:
            print('Asset updated successfully!')
        else:
            print(f'PUT request failed with code {response.status_code}.')

    #"clean"/simplify Intel-based CPUs
    def clean_cpu(model):
        match = re.search(cpu_pattern, model)
        if match:
            print("Reformatting CPU.")
            return match.group(3)
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


    #Clean CPU if attribute is found
    if attribute_dict['CPU Type'] is not None:
        cleaned_cpu = clean_cpu(attribute_dict['CPU Type'])
        attribute_dict['CPU Type'] = cleaned_cpu
    else:
        print('CPU already formatted or attribute not found.')
    #Clean battery if attribute is found
    if attribute_dict['Battery Wear Level'] is not None:
        cleaned_battery = clean_battery(attribute_dict['Battery Wear Level'])
        attribute_dict['Battery Wear Level'] = cleaned_battery
    else:
        print('Battery Wear Level already formatted or not found.')
    #Update dictionary to correct JSON format for Razor
    attribute_dict = [{'typeName': key, 'value': value} for key, value in attribute_dict.items() if value is not None]
    #ship payload once all operations are done
    payload = UGH!!!!
    print(payload)
    #ship_payload(payload)


#run all corrections on specified UID (main function)
main()
