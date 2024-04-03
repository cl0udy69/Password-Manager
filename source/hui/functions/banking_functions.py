def banking_selection():
    banking_choices = input('Would you like to save, view, edit, or delete?: ').lower()
    if banking_choices in user_choices['save_banking_choices']:
        save_banking()
    elif banking_choices in user_choices['see_banking_choices']:
        see_banking()
    elif banking_choices in user_choices['delete_banking_choices']:
        delete_banking()
    elif banking_choices in user_choices['edit_banking_choices']:
        edit_banking()
    else:
        print('Invalid Input')
        banking_selection()
        
def save_banking():
    bank = input('Bank: ')
    account = input('Account: ')
    routing = input('Routing: ')
    type_ = input('Account Type: ')
    website = input('Bank Website: ')
    phone_number = input('Phone Number: ')

    save_banking[bank] = {'account': account, 'routing': routing, 'type': type_, 'website': website, 'phone number': phone_number}

def see_banking():
    if not save_banking:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection in error_handling_positive['save_banking_choices']:
            save_banking()
        elif selection in error_handling_negative['dont_save_banking_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Banking Information: ')
        for bank, banking_info in save_banking.items():
            print(f'Bank: {bank}, Account: {banking_info["account"]}, Routing: {banking_info["routing"]}, Account Type: {banking_info["type"]}, Website: {banking_info["website"]}, Phone Number: {banking_info["phone number"]}')

def delete_banking(save_banking):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_banking:
        del save_banking[field_to_delete]
        print(f'{field_to_delete.capitaize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_changes in error_handling_positive['dont_delete_banking_choices']:
            save_banking_to_file(save_banking, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delete_banking_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
        
def edit_banking():
    print("Select the bank field you want to edit:")
    for bank, data in save_banking.items():
        print(bank)
        for field in data:
            print(f" - {field}")

    banking_to_edit = input('Enter the bank field you want to edit: ').lower()
    for bank, data in save_banking.items():
        if banking_to_edit in data:
            new_value = input(f'Enter the new value for {banking_to_edit}: ')
            save_banking[bank][banking_to_edit] = new_value
            print(f'{banking_to_edit.capitalize()} updated successfully')
            return  
        else:
            print('Field not found')
    else:
        print('Banking not found')