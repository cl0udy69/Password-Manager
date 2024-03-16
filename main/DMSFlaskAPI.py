from flask import Flask, jsonify, request
import json
import os
import random
import sys

app = Flask(__name__)

saved_logins = {}
saved_address = {}
saved_banking_info = {}
saved_ssn = {}
saved_phone_number = {}

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

@app.route('/save_login', methods=['POST'])
def save_login():
    data = request.json
    domain = data.get('domain')
    username = data.get('username')
    password = data.get('password')

    saved_logins[domain] = {'Username': username, 'Password': password}
    save_data_to_file()

    return jsonify({'message': 'Login saved successfully'})

# Add similar routes for other functionalities

if __name__ == '__main__':
    app.run(debug=True)


# http://localhost:5000/save_login

#This is a basic example, and you'll need to expand it for other functionalities like saving personal information, generating passwords, etc. You can create additional routes for each functionality, and the API can be accessed via HTTP requests.

#For example, to save a login, you can send a POST request to http://localhost:5000/save_login with JSON data containing the domain, username, and password.

#Remember to replace the code in the original functions with the appropriate Flask routes and logic.