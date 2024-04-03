def medical_selection():
    medical_choices = input('Would you like to save, view, delete, or edit?: ').lower()
    if medical_choices in user_choices['save_medical_choices']:
        save_medical()
    elif medical_choices in user_choices['see_medical_choices']:
        see_medical()
    elif medical_choices in user_choices['delete_medical_choices']:
        delete_medical()
    elif medical_choices in user_choices['edit_medical_choices']:
        edit_medical()
    else:
        print('Invalid input.')
        
def save_medical():
    condition = input('Medical Condition: ')
    diagnosis = input('Medical Diagnosis: ')
    name = input('Name of Medication: ')
    dosage = input('Dosage of Medication: ')
    allergies = input('Allergies: ')
    blood_type = input('Blood Type: ')
    illness = input('Chronic Illness: ')
    implants = input('Medical Devices or Implants: ')
    history = input('Medical History: ')

    save_medical[condition] = {'diagnosis': diagnosis, 'name': name, 'dosage': dosage, 'allergies': allergies, 'blood type': blood_type, 'illness': illness, 'implants': implants, 'history': history}

def see_medical():
    if not save_medical:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_medical_choices']:
            save_medical()
        elif selection in error_handling_negative['dont_save_medical_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Saved Medical')
        for condition, medical_info in save_medical.items():
            print(f'Medical Condition: {medical_info["condition"]}, Medical diagnosis: {medical_info["diagnosis"]}, Name of Medication: {medical_info["name"]}, Dosage of Medication: {medical_info["dosage"]}, Allergies: {medical_info["allergies"]}, Blood Type: {medical_info["blood type"]}, Chronic Illness: {medical_info["illness"]}, Medical Devices or Impants: {medical_info["implants"]}, Medical history: {medical_info["history"]}')

def delete_medical(save_medical):
    field_to_delete = input('Enter the field you want to delete: ').lower()
    if field_to_delete in save_medical:
        del save_medical[field_to_delete]
        print(f'{field_to_delete.capitalize()} deleted successfully')
        
        save_changes = input('Do you want to save the changes?: ').lower()
        if save_changes in error_handling_positive['dont_delete_medical_choices']:
            save_medical_to_file(save_medical, 'address.json')
            print('Changes saved.')
        elif save_changes in error_handling_negative['delete_medical_choices']:
            print('Changes discarded.')
        else:
            print('Invalid input. Changes discarded.')
    else:
        print('Field not found')
        
def edit_medical():
    print("Select the field you want to edit:")
    for medical, data in save_medical.items():
        print(medical)
        for field in medical:
            print(f" - {field}")
    
    medical_to_edit = input('Select the field you want to edit: ').lower()
    for medical, data in save_medical.items():
        if medical_to_edit in data:
            new_value = input(f'Enter the new value for {medical_to_edit}: ')
            save_medical[medical][medical_to_edit] = new_value
            print(f'{medical_to_Edit.capitalize()} updated successfully')
            return
        else:
            print('Field not found')
    else:
        print('Medical not found')