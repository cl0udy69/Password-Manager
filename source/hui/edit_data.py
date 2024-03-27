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

        

def edit_birth():
    
        

def edit_gender():
    


def edit_nationality():
    
        

def edit_occupation():
    
        

def edit_education():
    


def edit_medical():
    
        

def edit_insurance():
    
        

def edit_passport():
    
    

def edit_legal():
    
    

def edit_ethnicity():
    
