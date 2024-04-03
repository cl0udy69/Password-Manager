def ssn_selection():
    ssn_choices = input('Would you like to save, view, delete, or edit?: ').lower()
    if ssn_choices in user_choices['save_ssn_choices']:
        save_ssn()
    elif ssn_choices in user_choices['see_ssn_choices']:
        see_ssn()
    elif ssn_choices in user_choices['delete_ssn_choices']:
        delete_ssn()
    elif ssn_choices in user_choices['edit_ssn_choices']:
        edit_ssn()
        
def save_ssn():
    ssn = input('Social Security Number: ')

    save_ssn[ssn] = {'ssn': ssn}
    
def see_ssn():
    if not save_ssn:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection in error_handling_positive['save_ssn_choices']:
            save_ssn()
        elif selection in error_handling_negative['dont_save_ssn_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Social Security Number:')
        for ssn, ssn_info in save_ssn.items():
            print(f'Social Security Number: {ssn_info["ssn"]}')
            
def delete_ssn(save_ssn):
    field_to_delete = input('Enter the field you want to delete: ').lower() 
    if field_to_delete in save_ssn:
        del save_ssn[field_to_delete]
        print(f'{field_to_delete.capitalize()} delete successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_changes in error_handling_positive['dont_delete_ssn_choices']:
            save_ssn_to_file(save_ssn, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delet_ssn_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')

def edit_ssn():
    print("Select the field you want to edit:")
    for ssn, data in save_ssn.items():
        print(ssn)
        for field in ssn:
            print(f" - {field}")
            
    ssn_to_edit = inpt('Enter the field you want to edit: ').lower()
    for ssn, data in save_ssn.items():
        if ssn_to_edit in data:
            new_value = input(f'Enter the new value for {ssn_to_edit}: ')
            save_ssn[ssn][ssn_to_edit] = new_value
            print(f'{ssn_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Social secuirty number not found')