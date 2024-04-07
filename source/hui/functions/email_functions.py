from file_operations import save_data_to_file, load_data_from_file

def email_selection():
    email_choices = input('Would you like to save, view, delete, or edit?: ').lower()
    if email_choices in user_choices['save_email_choices']:
        save_email()
    elif email_choices in user_choices['see_email_choices']:
        see_email()
    elif email_choices in user_choices['delete_email_choices']:
        delete_email()
    elif email_choices in user_choices['edit_email_choices']:
        edit_email()
    else:
        print('Invalid input.')
        
    save_data_to_file(email_data, filename)
    
    loaded_data = load_data_from_file(filename)
    print("Loaded data ", loaded_data)

def save_email():
    email = input('Email: ')
    primary = input('Primary Email: ')
    business = input('Business Email: ')
    preferred = input('Preferred Email for Communication: ')

    save_email[email] = {'email': email, 'primary': primary, 'business': business, 'preferred': preferred}
    
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

def delete_email(save_email):
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
