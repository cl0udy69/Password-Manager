from file_operations import save_data_to_file, load_data_from_file

def nationality_selection():
    nationality_choices = input('Would you like to save, view, delete, or edit?: ').lower()
    if nationality_choices in user_choices['save_nationality_choices']:
        save_nationality()
    elif nationality_choices in user_choices['see_nationality_choices']:
        see_nationality()
    elif nationality_choices in user_choices['delete_nationality_choices']:
        delete_nationality()
    elif nationality_choices in user_choices['edit_nationality_choices']:
        edit_nationality()
    else:
        print('Invalid input.')
        
    save_data_to_file(nationality_data, filename)
    
    loaded_data = load_data_from_file(filename)
    print("Loaded data", loaded_data)
        
def save_nationality():
    nationality = input('Country: ')
    citizenship = input('Country of Citizenship: ')
    origin = input('National Origin: ')

    save_nationality[nationality] = {'nationality': nationality, 'citizenship': citizenship, 'origin': origin}
    
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
            
def delete_nationality(save_nationality):
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
        
def edit_nationality():
    print("Select the field you want to edit:")
    for nationality, data in save_nationality.items():
        print(nationality)
        for field in nationality:
            print(f" - {field}")
            
    nationality_to_edit = input('Enter the field you want to edit: ').lower()
    for nationality, data in save_nationality.items():
        if nationality_to_edit in data:
            new_value = input(f'Enter the new value for {nationality_to_edit}: ')
            save_nationality[nationality][nationality_to_edit] = new_value
            print(f'{nationality_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Nationality not found')
