from file_operations import save_data_to_file, load_data_from_file

def login_selection():
    login_choices = input('Would you like to save, view, delete, or edit?: ').lower()
    if login_choices in user_choices['save_login_choices']:
        save_login()
    elif login_choices in user_choices['see_login_choices']:
        see_login()
    elif login_chocies in user_choices['delete_login_choices']:
        delete_login()
    elif login_choices in user_choices['edit_login_choices']:
        edit_login()
    else:
        print('Invalid input.')
        
    save_data_to_file(legal_data, filename)
    
    loaded_data = load_data_from_file(filename)
    print("Loaded data", loaded_data)
        
def save_login():
    domain = input('Domain: ')
    username = input('Username: ')
    password = input('Password: ')
    type_ = input('Account Type: ')
    name = input('Account Name: ')

    save_login[domain] = {'Username': username, 'Password': password, 'type': type_, 'name': name}
    
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

def delete_login(save_login):
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
