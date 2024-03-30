import os
import json

DATA_FILE = 'save_data.json'

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as file:
        save_data = json.load(file)
        save_address = save_data.get('address', {})
        save_banking_info = save_data.get('banking_info', {})
        save_ssn = save_data.get('ssn', {})
        save_phone_number = save_data.get('phone_number', {})
        save_login = save_data.get('login', {})
        save_email = save_data.get('email', {})
        save_password = save_data.get('password', {})
        save_birth = save_data.get('birth', {})
        save_gender = save_data.get('gender', {})
        save_nationality = save_data.get('nationality', {})
        save_occupation = save_data.get('occupation', {})
        save_education = save_data.get('education', {})
        save_medical = save_data.get('medical', {})
        save_insurance = save_data.get('insurance', {})
        save_driving = save_data.get('driving', {})
        save_passport = save_data.get('passport', {})
        save_legal = save_data.get('legal', {})
        save_ethnicity = save_data.get('ethnicity', {})
        

def save_data_to_file():
    data_to_save = {
        'address': save_address,
        'banking_info': save_banking_info,
        'ssn': save_ssn,
        'phone_number': save_phone_number,
        'login' : save_login,
        'email' : save_email,
        'password' : save_password,
        'birth' : save_birth,
        'gender' : save_gender,
        'nationality' : save_nationality,
        'occupation' : save_occupation,
        'education' : save_education,
        'medical' : save_medical,
        'insurance' : save_insurance,
        'driving' : save_driving,
        'passport' : save_passport,
        'legal' : save_legal,
        'ethnicity' : save_ethnicity
        
    }
    with open(DATA_FILE, 'w') as file:
        json.dump(data_to_save, file)
