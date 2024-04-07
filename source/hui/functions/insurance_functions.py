from file_operations import save_data_to_file, load_data_from_file

def insurance_selection():
    insurance_choices = input('Would you like to save, view, delete, or edit?: ').lower()
    if insurance_choices in user_choices['save_insurance_choices']:
        save_insurance()
    elif insurance_choices in user_choices['see_insurance_choices']:
        see_address()
    elif insurance_choices in user_choices['delete_insurance_choices']:
        delete_insurance()
    elif insurance_choices in user_choices['edit_insurance_choices']:
        edit_insurance()
    else:
        print('Invalid input.')
        
    save_data_to_file(insurance_data, filenme)
    
    loaded_data = load_data_from_file(filename)
    print("Loaded data", loaded_data)
        
def save_insurance():
    name = input('Insurance company name: ')
    policy = input('Insurance policy number: ')
    number = input('Insurance group number: ')
    plan = input('Insurance plan type: ')
    effective_date = input('Insurance plan effective date: ')
    expiration_date = input('Insurance plan expiration date: ')
    detail = input('Insurance plan coverage details: ')
    insured = input('Assets Insured: ')
    deductible = input('Insurance plans deductible amount: ')
    co_payment = input('Insurance plans co-pay amount: ')

    save_insurance[name] = {'policy': policy, 'number': number, 'plan': plan, 'effective date': effective_date, 'expiration date': expiration_date, 'detail': detail, 'insured': insured, 'deductible': deductible, 'co-payment': co_payment}

def see_insurance():
    if not save_insurance:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_insurance_choices']:
            save_insurance()
        elif selection in error_handling_negative['dont_save_insurance_choices']:
            choices = input('What would you like to do?: ')
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Insurance')
        for name, insurance_info in save_insurance.items():
            print(f'Insurance company name: {insurance_info["name"]}, Insurance policy number: {insurance_info["policy"]}, Insurance group number: {insurance_info["number"]}, Insurance plan type: {insurance_info["plan"]}, Insurance plan effective date: {insurance_info["effective date"]}, Insurance plan expiration date: {insurance_info["expiration date"]}, Insurance plan coverage details: {insurance_info["detail"]}, Assets Insured: {insurance_info["insured"]}, Insurance plans deductible amount: {insurance_info["deductible"]}, Insurance plans co-pay amount: {insurance_info["co-payment"]}')

def delete_insurance(save_insurance):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_insurance:
        del save_insurance[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_changes in error_handling_positive['dont_delete_insurance_choices']:
            save_insurance_to_file(save_insurance, 'address.json')
            print('Changes saved')
        elif save_changes in error_handling_negative['delete_insurance_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
        
def edit_insurance():
    print("Select the field you want to edit:")
    for insurance, data in save_insurance.items():
        print(insurance)
        for field in insurance:
            print(f" - {field}")
            
    insurance_to_edit = input('Select the field you want to edit: ').lower()
    for insurance, data in save_insurance.items():
        if insurance_to_edit in data:
            new_value = input(f'Enter the new value for {insurance_to_edit}: ')
            save_insurance[insurance][insurance_to_edit] = new_value
            print(f'{insurance_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Insurance not found')
