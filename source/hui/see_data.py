def see_address():
    if not save_address:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection in error_handling_positive['save_address_choices']:
            save_address()
        elif selection in error_handling_negative['dont_save_address_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print("Invalid Input")
    else:    
        print('Saved address: ')
        for address, address_info in save_address.items():
            print(f'Street Address: {address}, State: {address_info["state"]}, City: {address_info["city"]}, Zipcode: {address_info["zipcode"]}, Apartment Number: {address_info["aptnumber"]}')

def see_banking():
    if not save_banking:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection in error_handling_positive['save_banking_choices']:
            save_banking()
        elif selection in error_handling_negative['dont_save_banking_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Banking Information: ')
        for bank, banking_info in save_banking.items():
            print(f'Bank: {bank}, Account: {banking_info["account"]}, Routing: {banking_info["routing"]}, Account Type: {banking_info["type"]}, Website: {banking_info["website"]}, Phone Number: {banking_info["phone number"]}')

def see_ssn():
    if not save_ssn:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection in error_handling_positive['save_ssn_choices']:
            save_ssn()
        elif selection in error_handling_negative['dont_save_ssn_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Social Security Number:')
        for ssn, ssn_info in save_ssn.items():
            print(f'Social Security Number: {ssn_info["ssn"]}')
            
def see_phone_number():
    if not save_phone_number:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection in error_handling_positive['save_phone_number_choices']:
            save_phone_number()
        elif selection in error_handling_negative['dont_save_phone_number_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Phone Number')
        for phone, phone_info in save_phone_number.items():
            print(f'Phone number: {phone_info["phone"]}, Primary Contact: {phone_info["primary"]}, Emergency Contacts: {phone_info["emergency"]}')
            
def see_login():
    if not save_login:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection in error_handling_positive['save_login_choices']:
            save_login()
        elif selection in error_handling_negative['dont_save_login_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Login')
        for domain, login_info in save_login.items():
            print(f'Domain: {domain}, Username: {login_info["Username"]}, Password: {login_info["Password"]}, Account Type: {login_info["type"]}, Account Name: {login_info["name"]}')
        
def see_email():
    if not save_email:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection in error_handling_positive['save_email_choices']:
            save_email()
        elif selection in error_handling_negative['dont_save_email_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else: 
            print('Invalid Input')
    else:
        print('Saved Email')     
        for email, email_info in save_email.items():
            print(f'Email: {email_info["email"]}, Primary Email: {email_info["primary"]}, Business Email: {email_info["business"]}, Preferred Email for Communication: {email_info["preferred"]}')
            
def see_password():
    if not save_password:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection in error_handling_positive['save_password_choices']:
            save_password()
        elif selection in error_handling_negative['dont_save_password_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else: 
            print('Invalid Input')
    else:
        print('Saved Password')
        for password, password_info in save_password.items():
            print(f'Password: {password_info["password"]}')
            
def see_birth():
    if not save_birth:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection in error_handling_positive['save_birth_choices']:
            save_birth()
        elif selection in error_handling_negative['dont_save_birth_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else: 
            print('Invalid Input')
    else:
        print('Saved Birthday')
        for day, birth_info in save_birth.items():
            print(f'Day: {day}, Month: {birth_info["month"]}, Year: {birth_info["year"]}')
            
def see_gender():
    if not save_gender:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_gender_choices']:
            save_gender()
        elif selection in error_handling_negative['dont_save_gender_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Gender')
        for sex, gender_info in save_gender.items():
            print(f'Sex: {gender_info["sex"]}, Gender: {gender_info["gender"]}, Pronouns: {gender_info["pronouns"]}')
            
def see_nationality():
    if not save_nationality:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_nationality_choices']:
            save_nationality()
        elif selection in error_handling_negative['dont_save_nationality_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Nationality')
        for nationality, nationality_info in save_nationality.items():
            print(f'Country: {nationality_info["nationality"]}, Country of Citizenship: {nationality_info["citizenship"]}, National Origin: {nationality_info["origin"]}')
            
def see_occupation():
    if not save_occupation:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_occupation_choices']:
            save_occupation()
        elif selection in error_handling_negative['dont_save_occupation_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Occupation')
        for title, occupation_info in save_occupation.items():
            print(f'Job Title: {occupation_info["title"]}, Company: {occupation_info["company"]}, Profession: {occupation_info["profession"]}, Years of Experience: {occupation_info["years of experience"]}')
            
def see_education():
    if not save_education:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_education_choices']:
            save_education()
        elif selection in error_handling_negative['dont_save_education_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Education')
        for level, education_info in save_education.items():
            print(f'Highest level of education: {education_info["level"]}, Highest degree earned: {education_info["degree"]}, Field of study: {education_info["field"]}')
        
def see_medical():
    if not save_medical:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_medical_choices']:
            save_medical()
        elif selection in error_handling_negative['dont_save_medical_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Medical')
        for condition, medical_info in save_medical.items():
            print(f'Medical Condition: {medical_info["condition"]}, Medical diagnosis: {medical_info["diagnosis"]}, Name of Medication: {medical_info["name"]}, Dosage of Medication: {medical_info["dosage"]}, Allergies: {medical_info["allergies"]}, Blood Type: {medical_info["blood type"]}, Chronic Illness: {medical_info["illness"]}, Medical Devices or Impants: {medical_info["implants"]}, Medical history: {medical_info["history"]}')

def see_insurance():
    if not save_insurance:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_insurance_choices']:
            save_insurance()
        elif selection in error_handling_negative['dont_save_insurance_choices']:
            choices = input('What would you like to do?: ')
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Insurance')
        for name, insurance_info in save_insurance.items():
            print(f'Insurance company name: {insurance_info["name"]}, Insurance policy number: {insurance_info["policy"]}, Insurance group number: {insurance_info["number"]}, Insurance plan type: {insurance_info["plan"]}, Insurance plan effective date: {insurance_info["effective date"]}, Insurance plan expiration date: {insurance_info["expiration date"]}, Insurance plan coverage details: {insurance_info["detail"]}, Assets Insured: {insurance_info["insured"]}, Insurance plans deductible amount: {insurance_info["deductible"]}, Insurance plans co-pay amount: {insurance_info["co-payment"]}')
       
def see_passport():
    if not save_passport:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_passport_choices']:
            save_passport()
        elif selection in error_handling_negative['dont_save_insurance_choices']:
            choices = input('What would you like to do?: ')
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Passport')
        for number, passport_info in save_passport.items():
            print(f'Passport number: {passport_info["number"]}, Date of Issue: {passport_info["date"]}, Date of Expiration: {passport_info["expiration"]}, Issuing Country: {passport_info["country"]}, Place of Issue: {passport_info["place"]}, Full Name: {passport_info["name"]}, Date of Birth: {passport_info["dob"]}, Gender: {passport_info["gender"]}, Nationality: {passport_info["nationality"]}, Restrictions or Limitations: {passport_info["restrictions"]}')
    
def see_legal():
    if not save_legal:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_legal_choices']:
            save_legal()
        elif selection in error_handling_negative['dont_save_legal_choices']:
            choices = input('What would you like to do?: ')
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved legal information')
        for issues, legal_info in save_legal.items():
            print(f'Legal Issues: {legal_info["issues"]} Legal Obligations or Restrictions: {legal_info["obligations"]} Legal Documents: {legal_info["documents"]}')
            
def see_ethnicity():
    if not save_ethnicity:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_ethnicity_choices']:
            save_ethnicity()
        elif selection in error_handling_negative['dont_save_ethnicity_choices']:
            choices = input('What would you like to do?: ')
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Ethnicity')
        for ethnicity, ethnicity_info in save_ethnicity.items():
            print(f'Ethnicity: {ethnicity_info["ethnicity"]}, Racial Background: {ethnicity_info["racial"]}, Cultural Background: {ethnicity_info["cultural"]}')

