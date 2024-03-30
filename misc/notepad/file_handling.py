import os
import json

DATA_FILE = 'save_data.json'

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as file:
        saved_data = json.load(file)
        saved_logins = saved_data.get('logins', {})
        saved_address = saved_data.get('address', {})
        saved_banking_info = saved_data.get('banking_info', {})
        saved_ssn = saved_data.get('ssn', {})
        saved_phone_number = saved_data.get('phone_number', {})

def save_data_to_file():
    data_to_save = {
        'logins': saved_logins,
        'address': saved_address,
        'banking_info': saved_banking_info,
        'ssn': saved_ssn,
        'phone_number': saved_phone_number
    }
    with open(DATA_FILE, 'w') as file:
        json.dump(data_to_save, file)
