from file_operations import save_data_to_file, load_data_from_file

def legal_selection():
    legal_choices = input('Would you like to save, view, delete, or edit?: ').lower()
    if legal_choices in user_choices['save_legal_choices']:
        save_legal()
    elif legal_choices in user_choices['see_legal_choices']:
        see_legal()
    elif legal_choices in user_choices['delete_legal_choices']:
        delete_legal()
    elif legal_choices in user_choices['edit_legal_choices']:
        edit_legal()
    else:
        print('Invalid input.')
        
    save_data_to_file(legal_data, filename)
    
    loaded_data = load_data_from_file(filename)
    print("Loaded data", loaded_data)

def save_legal():
    issues = input('Legal Issues: ')
    obligations = input('Legal Obligations or Restrictions: ')
    documents = input('legal Documents: ')

    save_legal[issues] = {'issues': issues, 'obligations': obligations, 'documents': documents}
    
def see_legal():
    if not save_legal:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_legal_choices']:
            save_legal()
        elif selection in error_handling_negative['dont_save_legal_choices']:
            choices = input('What would you like to do?: ')
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved legal information')
        for issues, legal_info in save_legal.items():
            print(f'Legal Issues: {legal_info["issues"]} Legal Obligations or Restrictions: {legal_info["obligations"]} Legal Documents: {legal_info["documents"]}')

def delete_legal(save_legal):
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
        
def edit_legal():
    print("Select the field you want to edit:")
    for legal, data in save_legal.items():
        print(legal)
        for field in legal:
            print(f" - {field}")
            
    legal_to_edit = input('Select the field you want to edit: ').lower()
    for legal, data in save_legal.items():
        if legal_to_edit in data:
            new_value = input(f'Enter the new value for {legal_to_edit}: ')
            save_legal[legal][legal_to_edit] = new_value
            print(f'{legal_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Legal information not found')
