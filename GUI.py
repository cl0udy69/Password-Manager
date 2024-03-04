import tkinter as tk
from tkinter import messagebox
import json
import os
import random
import sys

class DataManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Dorian's Data System")

        # Variables for user input
        self.domain_var = tk.StringVar()
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # Existing saved data
        self.saved_logins = {}
        self.saved_address = {}
        self.saved_banking_info = {}

        # Load saved data from file
        self.load_data_from_file()

        # Create frames for different options
        self.frames = {}
        self.create_frames()

        # Widgets
        self.create_widgets()

    entry_style = {'font': ('Arial', 12), 'bg': 'white', 'width': 20}

    def load_data_from_file(self):
        DATA_FILE = 'save_data.json'
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                saved_data = json.load(file)
                self.saved_logins = saved_data.get('logins', {})
                self.saved_address = saved_data.get('address', {})
                self.saved_banking_info = saved_data.get('banking_info', {})

    def save_data_to_file(self):
        DATA_FILE = 'save_data.json'
        data_to_save = {
            'logins': self.saved_logins,
            'address': self.saved_address,
            'banking_info': self.saved_banking_info
        }
        with open(DATA_FILE, 'w') as file:
            json.dump(data_to_save, file)

    def create_frames(self):
        # Create frames for different options
        for option in ['Save Login', 'Generate Password', 'Save Personal Information', 'Save Banking Info', 'See All Saved Logins', 'See All saved Address\'s', 'See All Saved Banking Information', 'See All Saved Data']:
            self.frames[option] = tk.Frame(self.root)

    def create_widgets(self):
        # Styling
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        label_style = {'font': ('Montserrat', 12), 'bg': '#f0f0f0'}
        button_style = {'font': ('Montserrat', 12), 'bg': '#4CAF50', 'fg': 'white', 'width': 15, 'height': 1}


        # Labels
        tk.Label(self.root, text="Select an option:", **label_style).pack(pady=10)

        # Buttons for different options
        options = ['Save Login', 'Generate Password', 'Save Personal Information', 'Save Banking Info', 'See All Saved Data']
        for option in options:
            tk.Button(self.root, text=option, command=lambda o=option: self.show_frame(o), **button_style).pack(pady=5)

        # Place frames
        for frame in self.frames.values():
            frame.pack_forget()

        # Initial frame to show
        self.show_frame('Save Login')

    def show_frame(self, option):
        # Show the selected frame
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[option].pack(fill=tk.BOTH, expand=True)

        # Handle specific frame content
        if option == 'Save Login':
            self.create_save_login_frame()
        elif option == 'Generate Password':
            self.create_generate_password_frame()
        elif option == 'Save Address':
            self.save_address_frame()
        elif option == 'Save Banking Info':
            self.save_banking_info_frame()
        elif option == 'See Saved Logins':
            self.see_saved_logins()
        elif option == 'See saved address':
            self.see_saved_address()

    def create_save_login_frame(self):
        print('Enter the login you would like to save:')
        domain = input('What domain does the login belong to? (e.g. Google, Facebook, Spotify, Steam): ')
        username = input('Username/Email: ')
        password = input('Password: ')

        self.saved_logins[domain] = {'Username': username, 'Password': password}

        tk.Label(self.frames['Save Login'], text="Domain:", **self.label_style).grid(row=0, column=0, sticky=tk.E, pady=5)
        tk.Entry(self.frames['Save Login'], textvariable=self.domain_var, **self.entry_style).grid(row=0, column=1, pady=5)
        tk.Label(self.frames['Save Login'], text="Username/Email:", **self.label_style).grid(row=1, column=0, sticky=tk.E, pady=5)
        tk.Entry(self.frames['Save Login'], textvariable=self.username_var, **self.entry_style).grid(row=1, column=1, pady=5)
        tk.Label(self.frames['Save Login'], text="Password:", **self.label_style).grid(row=2, column=0, sticky=tk.E, pady=5)
        tk.Entry(self.frames['Save Login'], textvariable=self.password_var, show='*', **self.entry_style).grid(row=2, column=1, pady=5)
        tk.Button(self.frames['Save Login'], text="Save Login", command=self.save_login, **self.button_style).grid(row=3, column=0, columnspan=2, pady=10)

    def create_generate_password_frame(self):
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
        pass

    def save_address_frame(self):
        # Your existing personal information code goes here
        pass

    def save_banking_info_frame(self):
        # Your existing banking info code goes here
        pass

    def see_saved_logins(self):
        # Your existing see all data code goes here
        pass

    def see_saved_address(self):
        # Your Existing see saved address code goes here
        pass

    def save_login(self):
        domain = self.domain_var.get()
        username = self.username_var.get()
        password = self.password_var.get()

        # Your existing code to save login information
        self.saved_logins[domain] = {'Username': username, 'Password': password}

        # Inform the user
        messagebox.showinfo("Saved", "Login information saved successfully.")

        # Save data to file
        self.save_data_to_file()


if __name__ == "__main__":
    root = tk.Tk()
    app = DataManagementSystem(root)
    root.mainloop()
