from file_operations import save_data_to_file, load_data_from_file

def password_selection():
    password_choices = input('Would you like to save, view, delete, or edit?: ').lower()
    if password_choices in user_choices['save_password_choices']:
        save_password
    elif password_choices in user_choices['see_password_choices']:
        see_password()
    elif password_choices in user_choices['delete_password_choices']:
        delete_password()
    elif password_choices in user_choices['edit_password_choices']:
        edit_password()
    else:
        print('Invalid input.')
        
    save_data_to_file([password_data, filename])
    
    loaded_data = load_data_from_file(filename)
    print("Loaded data", loaded_data)
        
def save_password():
    password = input('Password: ')

    save_password[password] = {'password': password}
    
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
            
def delete_password(save_password):
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
