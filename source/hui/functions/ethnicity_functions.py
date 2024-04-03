def ethnicity_selection():
    ethnicity_choices = input('Would you like to save, view, delete, or edit?: ').lower()
    if ethnicity_choices in user_chocices['save_ethnicity_choices']:
        save_ethnicity()
    elif ethnicity_choices in user_choices['see_ethnicity_choices']:
        see_ethnicity()
    elif ethnicity_choices in user_choices['delete_ethnicity_choices']:
        delete_ethnicity()
    elif ethnicity_choices in user_choices['edit_ethnicity_choices']:
        edit_ethnicity()
    else:
        print('Invalid input.')
        
def save_ethnicity():
    ethnicity = input('Ethnicity: ')
    racial = input('Racial Background: ')
    cultural = input('Cultural Background: ')

    save_ethnicity[ethnicity] = {'ethnicity': ethnicity, 'racial': racial, 'cultural': cultural}
    
def see_ethnicity():
    if not save_ethnicity:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_ethnicity_choices']:
            save_ethnicity()
        elif selection in error_handling_negative['dont_save_ethnicity_choices']:
            choices = input('What would you like to do?: ')
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Ethnicity')
        for ethnicity, ethnicity_info in save_ethnicity.items():
            print(f'Ethnicity: {ethnicity_info["ethnicity"]}, Racial Background: {ethnicity_info["racial"]}, Cultural Background: {ethnicity_info["cultural"]}')

def delete_ethnicity(save_ethnicity):
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

def edit_ethnicity():
    print("Select the field you want to edit:")
    for ethnicity, data in save_ethnicity.items():
        print(ethnicity)
        for field in ethnicity:
            print(f" - {field}")
            
    ethnicity_to_edit = input('Enter the field you want to edit: ').lower()
    for ethnicity, data in save_ethnicity.items():
        if ethnicity_to_edit in data:
            new_value = input(f'Enter the new value for {ethnicity_to_edit}: ')
            save_ethnicity[ethnicity][ethnicity_to_edit] = new_value
            print(f'{ethnicity_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Ethnicity not found')