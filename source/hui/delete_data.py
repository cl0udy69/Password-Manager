def delete_address_field(address):
    field_to_delete = input('Enter the field you would like to delete (e.g. State, Adress, Zipcode, Etc): ')
    if field_to_delete in save_address[address]:
        del save_address[address][field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
    else:
        print('Field not found')