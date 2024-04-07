from file_operations import save_data_to_file, load_data_from_file

def phone_number_selection():
    phone_number_choices = input('Would you like to save, view, delete, or edit?: ').lower()
    if phone_number_choices in user_choices['save_phone_number_choices']:
        save_phone_number()
    elif phone_number_choices in user_choices['see_phone_number_choices']:
        see_phone_number()
    elif phone_number_choices in user_choices['delete_phone_number_choices']:
        delete_phone_number()
    elif phone_number_choices in user_choices['edit_phone_number_choices']:
        edit_phone_number()
    else:
        print('Invalid input.')
        
    save_data_to_file(phone_number_data, filename)
    
    loaded_data = load_data_from_file(filename)
    print("Loaded data", loaded_data)
        
def save_phone_number():
    phone = input('Phone Number: ')
    primary = input('Primary Contact: ')
    emergency = input('Emergency Contacts: ')

    save_phone_number[phone] = {'phone': phone, 'primary': primary, 'emergency': emergency}
    
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
            
def delete_phone_number(save_phone_number):
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
