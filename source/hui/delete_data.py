def delete_address_field(save_address):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_address:
        del save_address[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')

        save_changes = input('Do you want to save the changes? (yes/no): ').lower()
        if save_changes in error_handling_positive['dont_delete_address_choices']:
            save_address_to_file(save_address, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delete_address_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
        
def delete_banking_field(save_banking):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_banking:
        del save_banking[field_to_delete]
        print(f'{field_to_delete.capitaize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_changes in error_handling_positive['dont_delete_banking_choices']:
            save_banking_to_file(save_banking, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delete_banking_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
        

def delete_ssn_field(save_ssn):
    field_to_delete = input('Enter the field you want to delete: ').lower() 
    if field_to_delete in save_ssn:
        del save_ssn[field_to_delete]
        print(f'{field_to_delete.capitalize()} delete successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_changes in error_handling_positive['dont_delete_ssn_choices']:
            save_ssn_to_file(save_ssn, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delet_ssn_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
        
        
def delete_phone_number_field(save_phone_number):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delet in save_phone_number:
        del save_phone_number[field_to_delete]
        print(f'{field_to_delete.capitalize()} updated successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_changes in error_handling_positive['dont_delet_phone_number_choices']:
            save_phone_number_to_file(save_phone_number, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delete_phone_number_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded')
    else:
        print('Field not found')
    

def delete_login_field(save_login):
    field_to_delete = input('Enter the field you want to delete: ').lower() 
    if field_to_delete in save_login:
        del save_login[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted succesfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_change in error_handling_positive['dont_delete_login_choices']:
            save_login_to_file(save_login, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delete_login_choices']:
            print('Changes discarded.')
        else:
            print('Invali input. Changes discarded.')
    else:
        print('Field not found')
    

def delete_email_field(save_email):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_email:
        del save_email[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Would you ;ike to save the changes?: ').lower()
        if save_changes in error_handling_positive['dont_delete_email_choices']:
            save_email_to_file(save_email, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delete_email_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
    

def delete_password_field(save_password):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_password:
        del save_password[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_changes in error_handling_positive['dont_delete_password_choices']:
            save_password_to_file(save_password, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delete_password_choices']:
            print('Changes discarded')
        else:
            print('Invalid input. Changes discarded')
    else:
        print('Field not found')
    

def delete_birth_field(save_birth):
    field_to_delete = input('Enter the field you want o delete: ').lower()
    if field_to_delete in save_birth:
        del save_birth[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes: ').lower()
        if save_changes in error_handling_positive['dont_delete_birth_choices']:
            save_birth_to_file(save_birth, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delet_birth_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
    

def delete_gender_field(save_gender):
    field_to_delete = input('Enter the field you want to edit: ').lower()
    if field_to_delete in save_gender:
        del save_gender[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes')
        if save_changes in error_handling_positive['dont_delete_gender_choices']:
            save_gender_to_file(save_gender, 'address.json')
            print('Changes saved')
        elif save_changes in error_handling_negative['delet_gender_choices']:
            print('Changes discarded')
        else:
            ('Invalid input. Changes discarded')
    else:
        print('Field not found')
    

def delete_nationality_field(save_nationality):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_nationality:
        del save_nationality[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_changes in error_handling_positive['dont_delete_nationality_choices']:
            save_nationality_to_file(save_nationality, 'address.json')
            print('Change saved.')
        elif save_changes in error_handling_negative['delet_nationality_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
    

def delete_occupation_field(save_occupation):
    field_to_delete = input('Enter the field you want to edit: ').lower()
    if field_to_Delete in save_occupation:
        del save_occupation[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_changes in erroe_handling_positive['dont_delete_occupation_choices']:
            save_occupation_to_file(save_occupation, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delete_occupation_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
    

def delete_education_field(save_education):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_education:
        del save_education[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_changes in error_handling_positive['dont_delete_education_choices']:
            save_education_to_file(save_education, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delete_education_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
    

def delete_medical_field(save_medical):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_medical:
        del save_medical[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_changes in error_handling_positive['dont_delete_medical_choices']:
            save_medical_to_file(save_medical, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delete_medical_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
    

def delete_insurance_field(save_insurance):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_insurance:
        del save_insurance[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_changes in error_handling_positive['dont_delete_insurance_choices']:
            save_insurance_to_file(save_insurance, 'address.json')
            print('Changes saved')
        elif save_changes in error_handling_negative['delete_insurance_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
    

def delete_driving_field(save_driving):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_driving:
        del save_driving[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_changes in error_handling_positive['dont_delete_driving_choices']:
            save_driving_to_file(save_driving, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delete_driving_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
    

def delete_legal_field(save_legal):
    field_to_delete = input('Enter the field you want to edit: ')
    if field_to_dele in save_legal:
        del save_legal[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_changes in error_handling_positive['dont_delete_legal_choices']:
            save_legal_to_file(save_legal, 'address.json')
            print('Change saved.')
        elif save_changes in error_handling_negative['delet_legal_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
    

def delete_ethnicity_field(save_ethnicity):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_ethnicity:
        del save_ethnicity[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes')
        if save_changes in error_handling_positive['dont_delete_ethnicity_choices']:
            save_ethnicity_to_file(save_ethnicity, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delete_ethnicity_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
