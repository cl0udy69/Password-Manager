import subprocess

file_names = [
    'address_function.py',
    'banking_function.py',
    'ssn_function.py',
    'phone_number_function.py',
    'login_function.py',
    'email_function.py',
    'password_function.py',
    'birth_function.py',
    'gender_function.py',
    'nationality_function.py',
    'occupation_function.py',
    'education_function.py',
    'medical_function.py',
    'insurance_function.py',
    'passport_function.py',
    'legal_function.py',
    'ethnicity_function.py',
]

for file_name in file_names:
    subprocess.run(['python', file_name])
