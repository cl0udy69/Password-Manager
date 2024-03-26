def edit_address():
    address_to_edit = input("Enter the street address you want to edit: ")
    if address_to_edit in save_address:
        field_to_edit = input("Enter the field you want to edit (state/city/zipcode/aptnumber): ").lower()
        if field_to_edit in save_address[address_to_edit]:
            new_value = input(f"Enter the new value for {field_to_edit}: ")
            save_address[address_to_edit][field_to_edit] = new_value
            print(f"{field_to_edit.capitalize()} updated successfully.")
        else:
            print("Field not found.")
    else:
        print("Address not found.")
        
def edit_banking(): 
    print("Select the bank field you want to edit:")
    for bank, data in save_banking.items():
        print(bank)
        for field in data:
            print(f" - {field}")

    banking_to_edit = input('Enter the bank field you want to edit: ').lower()
    for bank, data in save_banking.items():
        if banking_to_edit in data:
            new_value = input(f'Enter the new value for {banking_to_edit}: ')
            save_banking[bank][banking_to_edit] = new_value
            print(f'{banking_to_edit.capitalize()} updated successfully')
            return  
    print('Field not found')

        
def edit_ssn():
    ssn_to_edit = input('Enter the field you want to edit: ').lower()
    if ssn_to_edit in save_ssn:
        field_to_edit = input('Enter the field you want to edit: ').lower()
        if field_to_edit in save_ssn[ssn_to_edit]:
            new_value = input(f'Enter the new value for {field_to_edit}: ')
            save_ssn[ssn_to_edit][field_to_edit] = new_value
            print(f'{field_to_edit.capitalize()} updated successfully')
        else:
            print('Field not found')
    else:
        print('Banking not found')
        
def edit_phone_number():
    phone_number_to_edit = input('Enter the field you want to edit: ').lower()
    if phone_number_to_edit in save_phone_number:
        field_to_edit = input('Enter the field you want to edit: ').lower()
        if field_to_edit in save_phone_number[phone_number_to_edit]:
            new_value = input(f'Enter the new value for {field_to_edit}: ')
            save_phone_number[phone_number_to_edit][field_to_edit] = new_value
            print(f'{field_to_edit.capitalize()} updated successfully')
        else:
            print('Field not found')
    else:
        print('Social security number not found')
        
def edit_login():
    login_to_edit = input('Enter the field you want to edit: ').lower()
    if login_to_edit in save_login:
        field_to_edit = input('Enter the field you want to edit: ').lower()
        if field_to_edit in save_login[login_to_edit]:
            new_value = input(f'Enter the new value for {field_to_edit}: ')
            save_login[login_to_edit][field_to_edit] = new_value
            print(f'{field_to_edit.capitalize()} updated successfully')
        else:
            print('Field not found')
    else:
        print('Login not found')
        
def edit_email():
    email_to_edit = input('Enter the field you want to edit: ').lower()
    if email_to_edit in save_email:
        field_to_edit = input('Enter the field you want to edit: ').lower()
        if field_to_edit in save_email[email_to_edit]:
            new_value = input(f'Enter the new value for {field_to_edit}: ')
            save_email[email_to_edit][field_to_edit] = new_value
            print(f'{field_to_edit.capitalize()} updated successfully')
        else:
            print('Field not found')
    else:
        print('Email not found')

def edit_password():
    password_to_edit = input('Enter the field you want to edit: ').lower()
    if password_to_edit in save_password:
        field_to_edit = input('Enter the field you want to edit: ').lower()
        if field_to_edit in save_passwod[password_to_edit]:
            new_value = input(f'Enter the new value for {field_to_edit}: ')
            save_password[password_to_edit][field_to_edit] = new_value
            print(f'{field_to_edit.capitalize()} updated successfully')
        else:
            print('Field not found')
    else:
        print('Password not found')
        
def edit_birth():
    birth_to_edit = input('Enter the field you want to edit: ').lower()
    if birth_to_edit in save_birth:
        field_to_edit = input('Enter the field you want to edit: ').lower()
        if field_to_edit in save_birth[birth_to_edit]:
            new_value = input(f'Enter the new value for {field_to_edit}: ')
            save_birth[birth_to_edit][field_to_edit] = new_value
            print(f'{field_to_edit.capitalize()} updated successfully')
        else:
            print('Field not found')
    else:
        print('Date of birth not found')
        
def edit_gender():
    gender_to_edit = input('Enter the field you want to edit: ').lower()
    if gender_to_edit in save_gender:
        field_to_edit = input('Etner the fied you want to edit: ').lower()
        if field_to_edit in save_gender[gender_to_edit]:
            new_value = input(f'Enter the new value for {field_to_edit}: ')
            save_gender[gender_to_edit][field_to_edit] = new_value
            print(f'{field_to_edit.capitalize()} updated successfully')
        else:
            print('Field not found')
    else:
        ('Gender not found')

def edit_nationality():
    nationality_to_edit = input('Enter the field you want to edit: ').lower()
    if nationality_to_edit in save_nationality:
        field_to_edit = input('Enter the field you want to edit: ').lower()
        if field_to_edit in save_nationality[nationality_to_edit]:
            new_value = input(f'Enter the new value for {field_to_edit}: ')
            save_nationality[nationality_to_edit][field_to_edit] = new_value
            print(f'{field_to_edit.capitalize()} updated successfully')
        else:
            print('Field not found')
    else:
        print('Nationality not found')
        
def edit_occupation():
    occupation_to_edit = input('Enter the field you want to edit: ').lower()
    if occupation_to_edit in save_occupation:
        field_to_edit = input('Enter the field you want to edit: ').lower()
        if field_to_edit in save_occupation[occupation_to_edit]:
            new_value = input(f'Enter the new value for {field_to_edit}: ')
            save_occupation[occupation_to_edit][field_to_edit] = new_value
            print(f'{field_to_edit.capitalize()} updated successfully')
        else:
            print('Field not found')
    else:
        print('Occupation not found')
        
def edit_education():
    education_to_edit = input('Enter the field you want to edit: ').lower()
    if education_to_edit in save_education:
        field_to_edit = input('Enter the field you want to edit: ').lower()
        if field_to_edit in save_education[education_to_edit]:
            new_value = input(f'Enter the new value for {field_to_edit}: ')
            save_education[education_to_edit][field_to_edit] = new_value
            print(f'{field_to_edit.capitalize()} updated successfully')
        else:
            print('Field not found')
    else:
        print('Education not found')

def edit_medical():
    medical_to_edit = input('Enter the field you want to edit: ').lower()
    if medical_to_edit in save_medical:
        field_to_edit = input('Enter the field you want to edit: ').lower()
        if field_to_edit in save_medical[medical_to_edit]:
            new_value = input(f'Enter the new value for {field_to_edit}: ')
            save_medical[medical_to_edit][field_to_edit] = new_value
            print(f'{field_to_edit.capitalize()} updated successfully')
        else:
            print('Field not found')
    else:
        print('Medical not found')
        
def edit_insurance():
    insurance_to_edit = input('Enter the field you want to edit: ').lower()
    if insurance_to_edit in save_insurance:
        field_to_edit = input('Enter the field you want to edit: ').lower()
        if field_to_edit in save_insurance[insurance_to_edit]:
            new_value = input(f'Enter the new value for {field_to_edit}: ')
            save_insurance[insurance_to_edit][field_to_edit] = new_value
            print(f'{field_to_edit.capitalize()} updated successfully')
        else:
            print('Field not found')
    else:
        print('Insurance not found')
        
def edit_passport():
    passport_to_edit = input('Enter the field you want to edit: ').lower()
    if passport_to_edit in save_passport:
        field_to_edit = input('Enter the field you want to edit: ').lower()
        if field_to_edit in save_passport[passport_to_edit]:
            new_value = input(f'Enter the new value for {field_to_edit}: ')
            save_passport[passport_to_edit][field_to_edit] = new_value
            print(f'{field_to_edit.capitalize()} updated successfully')
        else:
            print('Field not found')
    else:
        print('Passport not found')
    
def edit_legal():
    
    
def edit_ethnicity():
    
