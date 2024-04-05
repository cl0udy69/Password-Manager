from file_operations import save_data_to_file, load_data_from_file

def education_selection():
    education_choices = input('Would you like to save, view, delete, or edit?: ').lower()
    if education_choices in user_choices['save_education_choices']:
        save_education()
    elif education_choices in user_choices['see_education_choices']:
        see_education()
    elif education_choices in user_choices['delete_education_choices']:
        delete_education()
    elif education_choices in user_choices['edit_education_choices']:
        edit_education()
    else:
        print('Invalid input.')
        
    save_data_to_file(education_data, filename)
    
    load_data = load_data_from_file(filename)
    print("Loaded data ", load_data)
        
def save_education():
    level = input('Highest level of education: ')
    degree = input('Highest degree earned: ')
    field = input('Field of Study: ')

    save_education[level] = {'level': level, 'degree': degree, 'field': field}
    
def see_education():
    if not save_education:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_education_choices']:
            save_education()
        elif selection in error_handling_negative['dont_save_education_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Education')
        for level, education_info in save_education.items():
            print(f'Highest level of education: {education_info["level"]}, Highest degree earned: {education_info["degree"]}, Field of study: {education_info["field"]}')

def delete_education(save_birth):
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
        
def edit_education():
    print("Select the field you want to edit:")
    for education, data in save_education.items():
        print(education)
        for field in education:
            print(f" - {field}")
            
    education_to_edit = input('Select the field you want to edit: ').lower()
    for education, data in save_education.items():
        if education_to_edit in data:
            new_value = input(f'Enter the new value for {education_to_edit}: ')
            save_education[education][education_to_edit] = new_value
            print(f'{education_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Education not found')
