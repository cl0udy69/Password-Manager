def personal_information_selection():
    print('Address\'s')
    print('Banking Information')
    print('Social Security Number')
    print('Phone Number')
    print('Login')
    print('Email')
    print('Password')
    print('Date of Birth')
    print('Gender')
    print('Nationality')
    print('Occupation')
    print('Education')
    print('Medical Information')
    print('Insurance Information')
    print('Driving Information')
    print('legal Information')
    print('Ethnicity')

    user_selection = input('Choose one of the following options: ')
    
    selection_functions = {
    'address_choices' : address_selection,
    'banking_choices' : banking_selection,
    'ssn_choices' : ssn_selection,
    'phone_number_choices' : phone_number_selection,
    'login_choices' : login_selection,
    'email_choices' : email_selection,
    'password_choices' : password_selection,
    'birth_choices' : birth_selection,
    'gender_choices' : gender_selection,
    'nationality_choices' : nationality_selection,
    'occupation_choices' : occupation_selection,
    'education_choices' : education_selection,
    'medical_choices' : medical_selection,
    'insurance_choices' : insurance_selection,
    'driving_choices' : driving_selection,
    'passport_choices' : passport_selection,
    'legal_choices' : legal_selection,
    'ethnicity_choices' : ethnicity_selection, 
}

    for key, value in user_choices.items():
        if user_selection.lower() in value:
            selection_functions[key]()
            break
    else:
        print("Invalid choice. Please try again.")
        personal_information_selection()

def address_selection():
    address_choices = input('Would you like to save, view, or delete?: ')
    if address_choices.lower() in user_choices['save_address_choices']:
        save_address()
    elif address_choices.lower() in user_choices['see_address_choices']:
        see_address()
    else:
        print('Invalid Choice')
        address_selection()

def banking_selection():
    banking_choices = input('Would you like to save, view, or delete?: ')
    if banking_choices.lower() in user_choices['save_banking_choices']:
        save_banking()
    elif banking_choices.lower() in user_choices['see_banking_choices']:
        see_banking()
    else:
        print('Invalid Choice')
        banking_selection()

def ssn_selection():
    ssn_choices = input('Would you like to save, view, or delete?: ')
    if ssn_choices.lower() in user_choices['save_ssn_choices']:
        save_ssn()
    elif ssn_choices.lower() in user_choices['see_ssn_choices']:
        see_ssn()
    else:
        print('Invalid Choice')
        ssn_selection()

def phone_number_selection():
    phone_number_choices = input('Would you like to save, view, or delete?: ')
    if phone_number_choices.lower() in user_choices['save_phone_number_choices']:
        save_phone_number()
    elif phone_number_choices.lower() in user_choices['see_phone_number_choices']:
        see_phone_number()
    else:
        print('Invalid Choice')
        phone_number_selection()

def login_selection():
    login_choices = input('Would you like to save, view, or delete?: ')
    if login_choices.lower() in user_choices['save_login_choices']:
        save_login()
    elif login_choices.lower() in user_choices['see_login_choices']:
        see_login()
    else:
        print('Invalid Choice')
        login_selection()

def email_selection():
    email_choices = input('Would you like to save, view, or delete?: ')
    if email_choices.lower() in user_choices['save_email_choices']:
        save_email()
    elif email_choices.lower() in user_choices['see_email_choices']:
        see_email()
    else:
        print('Invalid Choice')
        email_selection()
        
def password_selection():
    password_choices = input('Would you like to save, view, or delete?: ')
    if password_choices.lower() in user_choices['save_password_choices']:
        save_password()
    elif password_choices.lower() in user_choices['see_password_choices']:
        see_password()
    else:
        print('Invalid Choice')
        password_selection()

def birth_selection():
    birth_choices = input('Would you like to save, view, or delete?: ')
    if birth_choices.lower() in user_choices['save_birth_choices']:
        save_birth()
    elif birth_choices.lower() in user_choices['see_birth_choices']:
        see_birth()
    else:
        print('Invalid Choice')
        birth_selection()

def gender_selection():
    gender_choices = input('Would you likle to save, view, or delete?: ')
    if gender_choices.lower() in user_choices['save_gender_choices']:
        save_gender()
    elif gender_choices.lower() in user_choices['see_gender_choices']:
        see_gender()
    else:
        print('Invalid Choice')
        gender_selection()

def nationality_selection():
    nationality_choices = input('Would you like to save, view, or delete?: ')
    if nationality_choices.lower() in user_choices['save_nationality_choices']:
        save_nationality()
    elif nationality_choices.lower() in user_choices['see_nationality_choices']:
        see_nationality
    else:
        print('Invalid Choice')
        nationality_selection()

def occupation_selection():
    occupation_choices = input('Would you like to save, view, or delete?: ')
    if occupation_choices.lower() in user_choices['save_occupation_choices']:
        save_occupation()
    elif occupation_choices.lower() in user_choices['see_occupation_choices']:
        see_occupation()
    else:
        print('Invalid Choice')
        occupation_selection()

def education_selection():
    education_choices = input('Would you like to save, view, or delete?: ')
    if education_choices.lower() in user_choices['save_education_choices']:
        save_education()
    elif education_choices.lower() in user_choices['see_education_choices']:
        see_education()
    else:
        print('Invalid Choice')
        education_selection()

def medical_selection():
    medical_choices = input('Would you like to save, view, or delete?: ')
    if medical_choices.lower() in user_choices['save_medical_choices']:
        save_medical()
    elif medical_choices.lower() in user_choices['see_medical_choices']:
        see_medical()
    else:
        print('Invalid Choice')
        medical_selection()

def insurance_selection():
    insurance_choices = input('Would you like to save, view, or delete?: ')
    if insurance_choices.lower() in user_choices['save_insurance_choices']:
        save_insurance()
    elif insurance_choices.lower() in user_choices['see_insurance_choices']:
        see_insurance()
    else:
        print('Invalid Choice')
        insurance_selection()

def driving_selection():
    driving_choices = input('Would you like to save, view, or delete?: ')
    if driving_choices.lower() in user_choices['save_driving_choices']:
        save_driving()
    elif driving_choices.lower() in user_choices['see_driving_choices']:
        see_driving()
    else:
        print('Invalid Choice')
        driving_selection()

def passport_selection():
    passport_choices = input('Would you like to save, view, or delete?: ')
    if passport_choices.lower() in user_choices['save_passport_choices']:
        save_passport()
    elif passport_choices.lower() in user_choices['see_passport_choices']:
        see_passport()
    else:
        print('Invalid Choice')
        passport_selection()

def legal_selection():
    legal_choices = input('Would you like to save, view, or delete?: ')
    if legal_choices.lower() in user_choices['save_legal_choices']:
        save_legal()
    elif legal_choices.lower() in user_choices['see_legal_choices']:
        see_legal()
    else:
        print('Invalid Choice')
        legal_selection()

def ethnicity_selection():
    ethnicity_choices = input('Would you like to save, view, or delete?: ')
    if ethnicity_choices.lower() in user_choices['save_ethnicity_choices']:
        save_ethnicity()
    elif ethnicity_choices.lower() in user_choices['see_ethnicity_choices']:
        see_ethnicity()
    else:
        print('Invalid Choice')
        ethnicity_selection()