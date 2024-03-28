import random

def generate_passwords():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!$%^&*()_+-=[]{}|;:,.<>/?~'
    number = int(input('Amount of passwords: '))
    length = int(input('Length of password: '))
    special = input('What special characters would you like to delete: ')
    numbers = input('What numbers would you like to delete: ')
    lowercase = input('What lowercase letters would you like to delete: ')
    capitals = input('What capital letters would you like to delete: ')

    for pwd in range(number):  
        password = ''
        for pwd in range(length):
            char = random.choice(chars)
            if char not in special and char not in numbers and char not in lowercase and char not in capitals:
                password += char
        print(password)
        save_password = input('Would you like to save this password? (make sure to copy the password before hand): ')
        if save_password.lower in password_input['save_generated_password_choices']:
            
