def delete_address_field(save_address):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_address:
        del save_address[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes? (yes/no): ').lower()
        if save_changes == 'yes':
            # Save the modified data
            # Example: save_address_to_file(save_address)
            print('Changes saved.')
        elif save_changes == 'no':
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
        

def delete_ssn_field(save_ssn):
    field_to_delete = input('Enter the field you want to delete: ').lower() 
    if field_to_delete in save_ssn:
        del save_ssn[field_to_delete]
        print(f'{field_to_delete.capitalize()} delete successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        
        
def delete_phone_number_field(save_phone_number):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delet in save_phone_number:
        del save_phone_number[field_to_delete]
        print(f'{field_to_delete.capitalize()} updated successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
    

def delete_login_field(save_login):
    field_to_delete = input('Enter the field you want to delete: ').lower() 
    if field_to_delete in save_login:
        del save_login[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted succesfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
    

def delete_email_field(save_email):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_email:
        del save_email[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Would you ;ike to save the changes?: ').lower()
    

def delete_password_field(save_password):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_password:
        del save_password[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
    

def delete_birth_field(save_birth):
    field_to_delete = input('Enter the field you want o delete: ').lower()
    if field_to_delete in save_birth:
        del save_birth[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes: ').lower()
    

def delete_gender_field(save_gender):
    field_to_delete = input('Enter the field you want to edit: ').lower()
    if field_to_delete in save_gender:
        del save_gender[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes')
    

def delete_nationality_field(save_nationality):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_nationality:
        del save_nationality[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
    

def delete_occupation_field(save_occupation):
    field_to_delete = input('Enter the field you want to edit: ').lower()
    if field_to_Delete in save_occupation:
        del save_occupation[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
    

def delete_education_field(save_education):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_education:
        del save_education[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
    

def delete_medical_field(save_medical):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_medical:
        del save_medical[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
    

def delete_insurance_field(save_insurance):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_insurance:
        del save_insurance[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
    

def delete_driving_field(save_driving):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_driving:
        del save_driving[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
    

def delete_legal_field(save_legal):
    field_to_delete = input('Enter the field you want to edit: ')
    if field_to_dele in save_legal:
        del save_legal[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
    

def delete_ethnicity_field(save_ethnicity):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_ethnicity:
        del save_ethnicity[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes')
