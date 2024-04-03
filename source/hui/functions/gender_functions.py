def gender_selection():
    gender_choices = input('Would you like to save, view, delete, or edit?: ').lower()
    if gender_choice in user_choices['save_gender_choices']:
        save_gender()
    elif gender_choices in user_choices['see_gender_choices']:
        see_gender()
    elif gender_choices in user_choices['delete_gender_choices']:
        delete_gender()
    elif gender_choices in user_choices['edit_gender_choices']:
        edit_gender()
    else:
        print('Invalid input.')
        
def save_gender():
    sex = input('Sex: ')
    gender = input('Gender: ')
    pronouns = input('Pronouns:')

    save_gender[sex] = {'sex': sex, 'gender': gender, 'pronouns': pronouns}
    
def see_gender():
    if not save_gender:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_gender_choices']:
            save_gender()
        elif selection in error_handling_negative['dont_save_gender_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Gender')
        for sex, gender_info in save_gender.items():
            print(f'Sex: {gender_info["sex"]}, Gender: {gender_info["gender"]}, Pronouns: {gender_info["pronouns"]}')

def delete_gender_field(save_gender):
    field_to_delete = input('Enter the field you want to edit: ').lower()
    if field_to_delete in save_gender:
        del save_gender[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes')
        if save_changes in error_handling_positive['dont_delete_gender_choices']:
            save_gender_to_file(save_gender, 'address.json')
            print('Changes saved')
        elif save_changes in error_handling_negative['delet_gender_choices']:
            print('Changes discarded')
        else:
            ('Invalid input. Changes discarded')
    else:
        print('Field not found')
        
def edit_gender():
    print("Select the field you want to edit:")
    for gender, data in save_gender.items():
        print(gender)
        for field in gender:
            print(f" - {field}")
    
    gender_to_edit = input('Enter the field you want to edit: ').lower()
    for gender, data in save_gender.items():
        if gender_to_edit in data:
            new_value = input(f'Enter the new value for {gender_to_edit}: ')
            save_gender[gender][gender_to_edit] = new_value
            print(f'{gender_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Gender not found')