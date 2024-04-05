# Function to handle address selection
from file_operations import save_data_to_file, load_data_from_file

def address_selection():
    address_choices = input('What would you like to do with your addresses?: save, view, edit, or delete?: ')
    if address_choices.lower() in user_choices['save_address_choices']:
        save_address()
    elif address_choices.lower() in user_choices['see_address_choices']:
        see_address()
    elif address_choices.lower() in user_choices['delete_address_choices']:
        delete_address()
    elif address_choices.lower() in user_choices['edit_address_choices']:
        edit_address()
    else:
        print('Invalid Choice')
        address_selection()
        
    save_data_to_file(address_data, filename)

    loaded_data = load_data_from_file(filename)
    print("Loaded Data:", loaded_data)

def save_address():
    address = input('Street Address: ')
    state = input('State/province: ')
    city = input('City: ')
    zipcode = input('Zipcode: ')
    aptnumber = input('Apartment Number: ')

    save_address[address] = {'state': state, 'city': city, 'zipcode': zipcode, 'aptnumber': aptnumber}
    
def see_address():
    if not save_address:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection in error_handling_positive['save_address_choices']:
            save_address()
        elif selection in error_handling_negative['dont_save_address_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print("Invalid Input")
    else:    
        print('Saved address: ')
        for address, address_info in save_address.items():
            print(f'Street Address: {address}, State: {address_info["state"]}, City: {address_info["city"]}, Zipcode: {address_info["zipcode"]}, Apartment Number: {address_info["aptnumber"]}')

def delete_address():
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_address:
        del save_address[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')

        save_changes = input('Do you want to save the changes? (yes/no): ').lower()
        if save_changes in error_handling_positive['dont_delete_address_choices']:
            save_address_to_file(save_address, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delete_address_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')


def edit_address(save_address):
    print("Enter the field you want to edit:")
    for address, data in save_address.items():
        print(address)
        for field in data:
            print(f" - {field}")
            
    address_to_edit = input('Enter the field you want to edit: ').lower()
    for address, data in save_address.items():
        if address_to_edit in data:
            new_value = input(f'Enter the new value for {address_to_edit}: ')
            save_address[address][address_to_edit] = new_value
            print(f'{address_to_edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Address not found')
        


