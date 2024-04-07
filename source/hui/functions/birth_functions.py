from file_operations import save_data_to_file, load_data_from_file

def birth_selection():
    birth_choices = input('Would you like to save, view, delete, or edit?: ').lower()
    if birth_choices in user_choices['save_birth_choices']:
        save_birth()
    elif birth_choices in user_choices['see_birth_choices']:
        see_birth()
    elif birth_choices in user_choices['delete_birth_choices']:
        delete_birth()
    elif birth_choices in user_choices['edit_birth_choices']:
        edit_birth()
    else:
        print('Invalid input.')
        
    save_data_to_file(birth_data, filename)
    
    loaded_data = load_data_from_file(filename)
    print("Loaded data ", loaded_data)
        
def save_birth():
    day = input('Day: ')
    month = input('Month: ')
    year = input('Year: ')

    save_birth[day] = {'month': month, 'year': year}
    
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
            
def delete_birth(save_birth):
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
        
def edit_birth():
    print("Select the field you want to edit:")
    for birth, data in save_birth.items():
        print(birth)
        for field in birth:
            print(f" - {field}")
            
    birth_to_edit = input('Enter the field you want to edit: ').lower()
    for birth, data in save_birth.items():
        if birth_to_edit in data:
            new_value = input(f'Enter the new value for {birth_to_edit}: ')
            save_birth[birth][birth_to_edit] = new_value
            print(f'{birth_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Date of birth not found')
    
