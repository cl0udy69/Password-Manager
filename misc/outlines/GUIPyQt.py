import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QFormLayout, QInputDialog
import json
import os
import random

class DataManagementSystemApp(QWidget):
    def __init__(self):
        super().__init__()

        # Variables for user input
        self.domain_var = QLineEdit()
        self.username_var = QLineEdit()
        self.password_var = QLineEdit()

        # Variables for Generate Password frame
        self.amount_var = QLineEdit()
        self.length_var = QLineEdit()
        self.special_var = QLineEdit()
        self.numbers_var = QLineEdit()
        self.lowercase_var = QLineEdit()
        self.capitals_var = QLineEdit()

        # Existing saved data
        self.saved_logins = {}
        self.saved_address = {}
        self.saved_banking_info = {}

        # Load saved data from file
        self.load_data_from_file()

        # Create a single layout for content
        self.content_layout = QVBoxLayout(self)
        self.content_layout.setContentsMargins(20, 20, 20, 20)
        self.content_layout.setAlignment(Qt.AlignTop)

        # Initial content to show
        self.show_main_menu()

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

    def show_main_menu(self):
        # Clear existing content
        self.clear_content()

        # Show Main Menu
        title_label = QLabel("Select an option:")
        title_label.setStyleSheet("font-family: Impact; font-size: 18pt; color: white;")
        self.content_layout.addWidget(title_label)

        # Buttons for different options
        options = ['Save Login', 'Generate Password', 'Save Personal Information', 'Save Banking Info', 'See All Saved Data']
        for option in options:
            button = QPushButton(option, clicked=lambda o=option: self.show_content(o))
            button.setStyleSheet("font-family: Arial; font-size: 14pt; background-color: #E74C3C; color: white; width: 15em; height: 2em;")
            self.content_layout.addWidget(button)

    def show_content(self, option):
        # Clear existing content
        self.clear_content()

        # Add a back button
        back_button = QPushButton("Back", clicked=self.show_main_menu)
        back_button.setStyleSheet("font-family: Arial; font-size: 14pt; background-color: #E74C3C; color: white; width: 15em; height: 2em;")
        self.content_layout.addWidget(back_button)

        if option == 'Save Login':
            self.show_save_login_content()
        elif option == 'Generate Password':
            self.show_generate_password_content()
        elif option == 'Save Personal Information':
            self.show_personal_information_content()
        elif option == 'Save Banking Info':
            self.show_banking_info_content()
        elif option == 'See All Saved Data':
            self.show_see_all_data_content()

    def show_save_login_content(self):
        # Show Save Login content
        self.add_label_entry("Domain:", self.domain_var)
        self.add_label_entry("Username/Email:", self.username_var)
        self.add_label_entry("Password:", self.password_var)
        self.add_button("Enter Password", self.enter_password)
        self.add_button("Save Login", self.save_login)

    def show_generate_password_content(self):
        # Show Generate Password content
        self.add_label_entry("Amount of passwords:", self.amount_var, validator=QIntValidator())
        self.add_label_entry("Length of password:", self.length_var, validator=QIntValidator())
        self.add_label_entry("Special characters to exclude:", self.special_var)
        self.add_label_entry("Numbers to exclude:", self.numbers_var)
        self.add_label_entry("Lowercase letters to exclude:", self.lowercase_var)
        self.add_label_entry("Capital letters to exclude:", self.capitals_var)

        self.result_text = QTextEdit(self)
        self.result_text.setFixedHeight(100)
        self.result_text.setStyleSheet("font-family: Arial; font-size: 14pt; background-color: #ECF0F1; color: #2C3E50;")
        self.content_layout.addWidget(self.result_text)

        self.add_button("Generate Password", self.generate_passwords)

    def enter_password(self):
        password, ok = QInputDialog.getText(self, "Password Entry", "Enter Password:", QLineEdit.Password)
        if ok:
            self.password_var.setText(password)

    def show_personal_information_content(self):
        # Your existing personal information code goes here
        pass

    def show_banking_info_content(self):
        # Your existing banking info code goes here
        pass

    def show_see_all_data_content(self):
        # Your existing see all data code goes here
        pass

    def save_login(self):
        domain = self.domain_var.text()
        username = self.username_var.text()
        password = self.password_var.text()

        # Your existing code to save login information
        self.saved_logins[domain] = {'Username': username, 'Password': password}

        # Inform the user
        self.show_message("Saved", "Login information saved successfully.")

        # Save data to file
        self.save_data_to_file()

        # Go back to the initial content
        self.show_main_menu()

    def clear_content(self):
        # Clear existing content
        for i in reversed(range(self.content_layout.count())):
            widget = self.content_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

    def generate_passwords(self):
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!$%^&*()_+-=[]{}|;:,.<>/?~'
        number = int(self.amount_var.text())
        length = int(self.length_var.text())
        special = self.special_var.text()
        numbers = self.numbers_var.text()
        lowercase = self.lowercase_var.text()
        capitals = self.capitals_var.text()

        passwords = []

        for _ in range(number):
            password = ''
            for _ in range(length):
                char = random.choice(chars)
                if char not in special and char not in numbers and char not in lowercase and char not in capitals:
                    password += char
            passwords.append(password)

        self.result_text.setPlainText("\n".join(passwords))

    def add_label_entry(self, label_text, line_edit, validator=None):
        label = QLabel(label_text)
        label.setStyleSheet("font-family: Impact; font-size: 18pt; color: white;")
        entry = QLineEdit(self)
        entry.setStyleSheet("font-family: Arial; font-size: 14pt; background-color: #ECF0F1; color: #2C3E50;")
        entry.setFixedWidth(300)
        if validator:
            entry.setValidator(validator)
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(entry)
        self.content_layout.addLayout(layout)
        line_edit.append(entry)

    def add_button(self, button_text, callback):
        button = QPushButton(button_text, clicked=callback)
        button.setStyleSheet("font-family: Arial; font-size: 14pt; background-color: #E74C3C; color: white; width: 15em; height: 2em;")
        self.content_layout.addWidget(button)

    def show_message(self, title, message):
        # Display an information message box
        QInputDialog.showMessageBox(self, title, message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DataManagementSystemApp()
    ex.setWindowTitle("Dorian's Data System")  # Set the window title here
    ex.show()
    sys.exit(app.exec_())
