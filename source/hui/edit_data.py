def edit_address():
    print("Enter the field you want to edit:")
    for address, data in save_address.items():
        print(address)
        for field in data:
            print(f" - {field}")
            
    address_to_edit = input('Enter the field you want to edit: ').lower()
    for address, data in save_address.items():
        if address_to_edit in data:
            new_value = input(f'Enter the new value for {address_to_edit}: ')
            save_address[address][address_to_edit] = new_value
            print(f'{address_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Address not found')
        

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
        else:
            print('Field not found')
    else:
        print('Banking not found')

        
def edit_ssn():
    print("Select the field you want to edit:")
    for ssn, data in save_ssn.items():
        print(ssn)
        for field in ssn:
            print(f" - {field}")
            
    ssn_to_edit = inpt('Enter the field you want to edit: ').lower()
    for ssn, data in save_ssn.items():
        if ssn_to_edit in data:
            new_value = input(f'Enter the new value for {ssn_to_edit}: ')
            save_ssn[ssn][ssn_to_edit] = new_value
            print(f'{ssn_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Social secuirty number not found')
    

def edit_phone_number():
    print("Select the field you want to edit:")
    for phone_number, data in save_phone_number.items():
        print(phone_number)
        for field in phone_number:
            print(f" - {field}")
            
    phone_number_to_edit = input('Enter the field you want to edit: ').lower()
    for phone_number, data in save_phone_number.items():
        if phone_number_to_edit in data:
            new_value = input(f'Enter the new value for {phone_number_to_edit}: ')
            save_phone_number[phone_number][phone_number_to_edit] = new_value
            print(f'{phone_number_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Phone number not found')
    

def edit_login():
    print("Select the field you want to edit:")
    for login, data in save_login.items():
        print(login)
        for field in login:
            print(f" - {field}")
    
    login_to_edit = input('Enter the field you want to edit: ').lower()
    for login, data in save_login.items():
        if login_to_edit in data:
            new_value = input(f'Enter the new value for {login_to_edit}: ')
            save_login[login][login_to_edit] = new_value
            print(f'{login_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Login not found')
        

def edit_email():
    print("Select the field you want to edit:")
    for email, data in save_email.items():
        print(email)
        for field in email:
            print(f" - {field}")
    
    email_to_edit = input('Enter the field you want to edit: ').lower()
    for email, data in save_email.items():
        if email_to_edit in data:
            new_value = input(f'Enter the new value for {email_to_edit}: ')
            save_email[email][email_to_edit] = new_value
            print(f'{email_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Email not found')


def edit_password():
    print("Select the field you want to edit:")
    for password, data in save_password.items():
        print(password) 
        for field in password:
            print(f" - {field}")
            
    password_to_edit = input('Enter the field you want to edit: ').lower()
    for password, data in save_password.items():
        if password_to_edit in data:
            new_value = input(f'Enter the new value for {password_to_edit}: ')
            save_password[password][password_to_edit] = new_value
            print(f'{password_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Password not found')
        

def edit_birth():
    print("Select the field you want to edit:")
    for birth, data in save_birth.items():
        print(birth)
        for field in birth:
            print(f" - {field}")
            
    birth_to_edit = input('Enter the field you want to edit: ').lower()
    for birth, data in save_birth.items():
        if birth_to_edit in data:
            new_value = input(f'Enter the new value for {birth_to_edit}: ')
            save_birth[birth][birth_to_edit] = new_value
            print(f'{birth_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Date of birth not found')
        

def edit_gender():
    print("Select the field you want to edit:")
    for gender, data in save_gender.items():
        print(gender)
        for field in gender:
            print(f" - {field}")
    
    gender_to_edit = input('Enter the field you want to edit: ').lower()
    for gender, data in save_gender.items():
        if gender_to_edit in data:
            new_value = input(f'Enter the new value for {gender_to_edit}: ')
            save_gender[gender][gender_to_edit] = new_value
            print(f'{gender_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Gender not found')


def edit_nationality():
    print("Select the field you want to edit:")
    for nationality, data in save_nationality.items():
        print(nationality)
        for field in nationality:
            print(f" - {field}")
            
    nationality_to_edit = input('Enter the field you want to edit: ').lower()
    for nationality, data in save_nationality.items():
        if nationality_to_edit in data:
            new_value = input(f'Enter the new value for {nationality_to_edit}: ')
            save_nationality[nationality][nationality_to_edit] = new_value
            print(f'{nationality_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Nationality not found')
        

def edit_occupation():
    print("Select the field you want to edit:")
    for occupation, data in save_occupation.items():
        print(occupation)
        for field in occupation:
            print(f" - {field}")
            
    occupation_to_edit = input('Select the field you want to edit: ').lower()
    for occupation, data in save_occupation.items():
        if occupation_to_edit in data:
            new_value = input(f'Enter the new value for {occupation_to_edit}: ')
            save_occupation[occupation][occupation_to_edit] = new_value
            print(f'{occupation_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Occupation not found')
        

def edit_education():
    print("Select the field you want to edit:")
    for education, data in save_education.items():
        print(education)
        for field in education:
            print(f" - {field}")
            
    education_to_edit = input('Select the field you want to edit: ').lower()
    for education, data in save_education.items():
        if education_to_edit in data:
            new_value = input(f'Enter the new value for {education_to_edit}: ')
            save_education[education][education_to_edit] = new_value
            print(f'{education_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Education not found')
            

def edit_medical():
    print("Select the field you want to edit:")
    for medical, data in save_medical.items():
        print(medical)
        for field in medical:
            print(f" - {field}")
    
    medical_to_edit = input('Select the field you want to edit: ').lower()
    for medical, data in save_medical.items():
        if medical_to_edit in data:
            new_value = input(f'Enter the new value for {medical_to_edit}: ')
            save_medical[medical][medical_to_edit] = new_value
            print(f'{medical_to_Edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Medical not found')
    
        
def edit_insurance():
    print("Select the field you want to edit:")
    for insurance, data in save_insurance.items():
        print(insurance)
        for field in insurance:
            print(f" - {field}")
            
    insurance_to_edit = input('Select the field you want to edit: ').lower()
    for insurance, data in save_insurance.items():
        if insurance_to_edit in data:
            new_value = input(f'Enter the new value for {insurance_to_edit}: ')
            save_insurance[insurance][insurance_to_edit] = new_value
            print(f'{insurance_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Insurance not found')
        

def edit_passport():
    print("Select the field you want to edit:")
    for passport, data in save_passport.items():
        print(passport)
        for field in passport:
            print(f" - {field}")
            
    passport_to_edit = input('Select the field you want to edit: ').lower()
    for passport, data in save_passport.items():
        if passport_to_edit in data:
            new_value = input(f'enter the new value for {passport_to_edit}: ')
            save_passport[passport][passport_to_edit] = new_value
            print(f'{passport_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Passport not found')
    

def edit_legal():
    print("Select the field you want to edit:")
    for legal, data in save_legal.items():
        print(legal)
        for field in legal:
            print(f" - {field}")
            
    legal_to_edit = input('Select the field you want to edit: ').lower()
    for legal, data in save_legal.items():
        if legal_to_edit in data:
            new_value = input(f'Enter the new value for {legal_to_edit}: ')
            save_legal[legal][legal_to_edit] = new_value
            print(f'{legal_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Legal information not found')
    

def edit_ethnicity():
    print("Select the field you want to edit:")
    for ethnicity, data in save_ethicity.items():
        print(ethnicity)
        for field in ethnicity:
            print(f" - {field}")
            
    ethnicity_to_edit = input('Enter the field you want to edit: ').lower()
    for ethnicity, data in save_ethnicity.items():
        if ethnicity_to_edit in data:
            new_value = input(f'Enter the new value for {ethnicity_to_edit}: ')
            save_ethnicity[ethnicity][ethnicity_to_edit] = new_value
            print(f'{ethnicity_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Ethnicity not found')
    
