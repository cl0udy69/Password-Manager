from file_operations import save_data_to_file, load_data_from_file

def occupation_selection():
    occupation_choices = input('Would you like to save, view, delete, or edit?: ').lower()
    if occupation_choices in user_choices['save_occupation_choices']:
        save_occupation()
    elif occupation_choices in user_choices['see_occupation_choices']:
        see_occupation()
    elif occupation_choices in user_choices['delete_occupation_choices']:
        delete_occupation()
    elif occupation_choices in user_choices['edit_occupation_choices']:
        edit_occupation()
    else:
        print('Invalid input.')
        
    save_data_to_file(occupation_data, filename)
    
    loaded_data = load_data_from_file(filename)
    print("Loaded data", loaded_data)
        
def save_occupation():
    title = input('Job Title: ')
    company = input('Company: ')
    profession = input('Profession: ')
    years_of_experience = input('Years of Experience: ')

    save_occupation[title] = {'title': title, 'company': company, 'profession': profession, 'years of experience': years_of_experience}
    
def see_occupation():
    if not save_occupation:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_occupation_choices']:
            save_occupation()
        elif selection in error_handling_negative['dont_save_occupation_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Occupation')
        for title, occupation_info in save_occupation.items():
            print(f'Job Title: {occupation_info["title"]}, Company: {occupation_info["company"]}, Profession: {occupation_info["profession"]}, Years of Experience: {occupation_info["years of experience"]}')
            
def delete_occupation(save_occupation):
    field_to_delete = input('Enter the field you want to edit: ').lower()
    if field_to_Delete in save_occupation:
        del save_occupation[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_changes in erroe_handling_positive['dont_delete_occupation_choices']:
            save_occupation_to_file(save_occupation, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delete_occupation_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
        
def edit_occupation():
    print("Select the field you want to edit:")
    for occupation, data in save_occupation.items():
        print(occupation)
        for field in occupation:
            print(f" - {field}")
            
    occupation_to_edit = input('Select the field you want to edit: ').lower()
    for occupation, data in save_occupation.items():
        if occupation_to_edit in data:
            new_value = input(f'Enter the new value for {occupation_to_edit}: ')
            save_occupation[occupation][occupation_to_edit] = new_value
            print(f'{occupation_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Occupation not found')
