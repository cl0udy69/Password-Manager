def save_address_to_file(address_data, filename):
    with open(filename, 'w') as file:
        json.dump(address_data, file, indent=4)
        
def save_banking_to_file(banking_data, filename):
    with open(filename, 'w') as file:
        json.dump(banking_data, file, indent=4)
        
def save_ssn_to_file(ssn_data, filename):
    with open(filename, 'w') as file:
        json,dump(ssn_data, file, indent=4)
        
def save_phone_number_to_file(phone_number_data, filename):
    with open(filename, 'w') as file:
        json.dump(phone_number_data, file, indent=4)
        
def save_login_to_file(loing_data, filename):
    with open(filename, 'w') as file:
        json.dump(login_data, file, indent=4)
        
def save_email_to_file(email_data, filename):
    with open(filename, 'w') as file:
        json.dump(email_data, file, indent=4)

def save_password_to_file(password_data, filename):
    with open(filename, 'w') as file:
        json.dump(password_data, file, indent=4)
        
def save_birth_to_file(birth_data, filename):
    with open(filename, 'w') as file:
        json.dump(birth_data, file, indent=4)
        
def save_gender_to_file(gender_data, filename):
    with open(filename, 'w') as file:
        json.dump(gender_data, file, indent=4)
        
def save_nationality_to_file(nationality_data, filename):
    with open(filename, 'w') as file:
        json.dump(nationality_data, file, indent=4)
        
def save_occupation_to_file(occupation_data, filename):
    with open(filename, 'w') as file:
        json.dump(occupation_data, file, indent=4)
        
def save_education_to_file(education_data, filename):
    with open(filename, 'w') as file:
        json.dump(education_data, file, indent=4)
        
def save_medical_to_file(medical_data, filename):
    with open(filename, 'w') as file:
        json.dump(medical_data, file, indent=4)
        
def save_insurance_to_file(insurance_data, filename):
    with open(filename, 'w') as file:
        json.dump(insurance_data, file, indent=4)
        
def save_legal_to_file(legal_data, filename):
    with open(filename, 'w') as file:
        json.dump(legal_data, file, indent=4)
        
def save_ethnicity_to_file(ethnicity_data, filename):
    with open(filename, 'w') as file:
        json.dump(ethnicity, file, indent=4)
        


def load_address_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    


save_address_data = load_address_from_file('address.json')
user_file_choices = ['save', 'edit', 'delete']