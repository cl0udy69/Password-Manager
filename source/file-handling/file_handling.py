import os
import json

DATA_FILE = 'save_data.json'

def load_data_from_file():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    else:
        return {
            'address': {},
            'banking_info': {},
            'ssn': {},
            'phone_number': {},
            'login': {},
            'email': {},
            'password': {},
            'birth': {},
            'gender': {},
            'nationality': {},
            'occupation': {},
            'education': {},
            'medical': {},
            'insurance': {},
            'driving': {},
            'passport': {},
            'legal': {},
            'ethnicity': {}
        }

def save_data_to_file(data_to_save):
    with open(DATA_FILE, 'w') as file:
        json.dump(data_to_save, file, indent=4)

def edit_data_field(data, field_name, new_value):
    data[field_name] = new_value
    print(f'{field_name.capitalize()} updated successfully')

def delete_data_field(data, field_name):
    if field_name in data:
        del data[field_name]
        print(f'{field_name.capitalize()} deleted successfully')
    else:
        print('Field not found')


saved_data = load_data_from_file()

edit_data_field(saved_data['address'], 'field', 'new_value')
edit_data_field(saved_data['banking_info'], 'field, new_value')
edit_data_field(saved_data['ssn'], 'field', 'new_value')
edit_data_field(saved_data['phone_number'], 'field', 'new_value')
edit_data_field(saved_data['login'], 'field', 'new_value')
edit_data_field(saved_data['email'], 'field', 'new_value')
edit_data_field(saved_data['password'], 'field', 'new_value')
edit_data_field(saved_data['birth'], 'field', 'new_value')
edit_data_field(saved_data['gender'], 'field', 'new_value')
edit_data_field(saved_data['nationality'], 'field', 'new_value')
edit_data_field(saved_data['occupation'], 'field', 'new_value')
edit_data_field(saved_data['education'], 'field', 'new_value')
edit_data_field(saved_data['medical'], 'field', 'new_value')
edit_data_field(saved_data['insurance'], 'field', 'new_value')
edit_data_field(saved_data['driving'], 'field', 'new_value')
edit_data_field(saved_data['passport'], 'field', 'new_value')
edit_data_field(saved_data['legal'], 'field', 'new_value')
edit_data_field(saved_data['ethnicity'], 'field', 'new_value')

delete_data_field(saved_data['address'], 'field')
delete_data_field(saved_data['banking_info'], 'field')
delete_data_field(saved_data['ssn'], 'field')
delete_data_field(saved_data['phone_number'], 'field')
delete_data_field(saved_data['login'], 'field')
delete_data_field(saved_data['password'], 'field')
delete_data_field(saved_data['email'], 'field')
delete_data_field(saved_data['password'], 'field')
delete_data_field(saved_data['birth'], 'field')
delete_data_field(saved_data['gender'], 'field')
delete_data_field(saved_data['nationality'], 'field')
delete_data_field(saved_data['occupation'], 'field')
delete_data_field(saved_data['education'], 'field')
delete_data_field(saved_data['medical'], 'field')
delete_data_field(saved_data['insurance'], 'field')
delete_data_field(saved_data['driving'], 'field')
delete_data_field(saved_data['passport'], 'field')
delete_data_field(saved_data['legal'], 'field')
delete_data_field(saved_data['ethnicity'], 'field')





save_data_to_file(saved_data)
