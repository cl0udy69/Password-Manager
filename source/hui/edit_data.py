def edit_address():
    address_to_edit = input("Enter the street address you want to edit: ")
    if address_to_edit in save_address:
        field_to_edit = input("Enter the field you want to edit (state/city/zipcode/aptnumber): ").lower()
        if field_to_edit in save_address[address_to_edit]:
            new_value = input(f"Enter the new value for {field_to_edit}: ")
            save_address[address_to_edit][field_to_edit] = new_value
            print(f"{field_to_edit.capitalize()} updated successfully.")
        else:
            print("Field not found.")
    else:
        print("Address not found.")
