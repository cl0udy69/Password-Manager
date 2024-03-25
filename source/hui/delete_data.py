def delete_address_field(address):
    field_to_delete = input('Enter the field you would like to delete (e.g. State, Adress, Zipcode, Etc): ').lower()
    if field_to_delete in save_address[address]:
        del save_address[address][field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
    else:
        print('Field not found')
        
def delete_banking_field():
    field_to_delete = input('Enter the field you would like to delete: ').lower()
    if fieled_to_delete in save_bankkng[banking]:
        del save_banking[banking][field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
    else:
        print('Field not found')

def delete_ssn_field():
    field_to_delete = input('Enter the field you would like to delete: ').lower()
    if field_to_delete in save_ssn[ssn]:
        del save_ssn[ssn][field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted succesfully')
    else:
        print('Field not found')
        
def delete_phone_number_field():
    field_to_delete = input('Enter the field you would like to delete').lower()
    if field_to_delte in save_phone_number[phone_number]:
        del save_phone_number[phone_number][field_to_delete]
        print(f'{field_to_delete.capitalize()} delete succesfully')
    else:
        print('Field not found')
        
def delete_login_field():
    field_to_delete = input('Enter the field you would like to delete: ').lower()
    if field_to_delete in save_login[logni]:
        del save_login[login][field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
    else:
        print('Field not found')
        
def delete_email_field():
    field_to_delete = input('Enter the field you would like to delete: ').lower()
    if field_to_delete in save_email[email]:
        del save_email[email][field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
    else:
        print('Field not found')
    
def delete_password_field():
    field_to_delete = input('Enter the field you would like to delete: ').lower()
    if field_to_delete in save_password[password]:
        del save_password[password][field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
    else:
        print('Field not found')
        
def delete_birth_field():
    field_to_delete = input('Enter the field you would like to delete: ').lower()
    if field_to_delete in save_birth[birth]:
        del save_birth[birth][field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
    else:
        print('Field not found')
        
def delete_gender_field():
    field_to_delete = input('Enter the field you would like to delete: ').lower()
    if field_to_delete in save_gender[gender]:
        del save_gender[gender][field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
    else:
        print('Field not found')
        
def delete_nationality_field():
    field_to_delete = input('Enter the fieled you would like to delete: ').lower()
    if field_to_delete in save_nationality[nationality]:
        del save_nationality[nationality][field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
    else:
        print('Field not found')
        
def delete_occupation_field():
    field_to_delete = input('Enter the field you would like to delete: ').lower()
    if field_to_delete in save_occupation[occupation]:
        del save_occupation[occupation][field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
    else:
        print('Field not found')
        
def delete_education_field():
    field_to_delete = input('Enter the field you would like to delete: ').lower()
    if field_to_delete in save_education[education]:
        del save_education[education][field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
    else:
        print('Field not found')

def delete_medical_field():
    field_to_delete = input('Enter the field you would like to delete: ').lower()
    if field_to_delete in save_medical[medical]:
        del save_medical[medica][field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
    else:
        print('Field not found')
        
def delete_insurance_field():
    field_to_delete = input('Enter the field you would like to delete: ').lower()
    if field_to_delete in save_insurance[insurance]:
        del save_insurance[insurance][field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
    else:
        print('Field not found')
        
def delete_passport_field():
    field_to_delete = input('Enter the field you would like to delete: ').lower()
    if field_to_delete in save_pasport[passport]:
        del save_passport[passport][field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
    else:
        print('Field not found')
        
def delete_legal_field():
    field_to_delete = input('Enter the field you would like to delete: ').lower()
    if field_to_delete in save_legal[legal]:
        del save_legal[legal][field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
    else:
        print('Field not found')
        
def delete_ethnicity_field():
    field_to_delete = input('Enter the field would like to delete: ').lower()
    if field_to_delete in save_ethnicity[ethnicity]:
        del save_ethnicity[ethnicity][field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully ')
