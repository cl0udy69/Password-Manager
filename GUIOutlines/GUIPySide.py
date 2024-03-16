import sys
import os
import json
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QTextEdit, QInputDialog, QMessageBox


class DataManagementSystem(QMainWindow):
    def __init__(self):
        super(DataManagementSystem, self).__init__()

        self.setWindowTitle("Dorian's Data System")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #3498DB;")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

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
        label = QLabel("Select an option:")
        label.setStyleSheet("font-size: 18px; font-family: Impact; background-color: #3498DB; color: white;")
        self.layout.addWidget(label)

        # Buttons for different options
        options = ['Save Login', 'Generate Password', 'Save Personal Information', 'Save Banking Info', 'See All Saved Data']
        for option in options:
            button = QPushButton(option, clicked=lambda o=option: self.show_content(o))
            button.setStyleSheet("font-size: 14px; font-family: Arial; background-color: #E74C3C; color: white; width: 15em; height: 2em;")
            self.layout.addWidget(button)

    def show_content(self, option):
        # Clear existing content
        self.clear_content()

        # Add a back button
        back_button = QPushButton("Back", clicked=self.show_main_menu)
        back_button.setStyleSheet("font-size: 14px; font-family: Arial; background-color: #E74C3C; color: white; width: 15em; height: 2em;")
        self.layout.addWidget(back_button)

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
        self.layout.addWidget(QLabel("Domain:"))
        self.layout.addWidget(self.domain_var)
        self.layout.addWidget(QLabel("Username/Email:"))
        self.layout.addWidget(self.username_var)
        self.layout.addWidget(QLabel("Password:"))
        enter_password_button = QPushButton("Enter Password", clicked=self.enter_password)
        enter_password_button.setStyleSheet("font-size: 14px; font-family: Arial; background-color: #E74C3C; color: white; width: 15em; height: 2em;")
        self.layout.addWidget(enter_password_button)

        save_login_button = QPushButton("Save Login", clicked=self.save_login)
        save_login_button.setStyleSheet("font-size: 14px; font-family: Arial; background-color: #E74C3C; color: white; width: 15em; height: 2em;")
        self.layout.addWidget(save_login_button)

    def show_generate_password_content(self):
        # Show Generate Password content
        self.layout.addWidget(QLabel("Amount of passwords:"))
        self.layout.addWidget(self.amount_var)
        self.layout.addWidget(QLabel("Length of password:"))
        self.layout.addWidget(self.length_var)
        self.layout.addWidget(QLabel("Special characters to exclude:"))
        self.layout.addWidget(self.special_var)
        self.layout.addWidget(QLabel("Numbers to exclude:"))
        self.layout.addWidget(self.numbers_var)
        self.layout.addWidget(QLabel("Lowercase letters to exclude:"))
        self.layout.addWidget(self.lowercase_var)
        self.layout.addWidget(QLabel("Capital letters to exclude:"))

        self.result_text = QTextEdit()
        self.result_text.setFixedHeight(100)
        self.result_text.setStyleSheet("font-size: 14px; font-family: Arial; background-color: #ECF0F1; color: #2C3E50;")
        self.layout.addWidget(self.result_text)

        generate_password_button = QPushButton("Generate Password", clicked=self.generate_passwords)
        generate_password_button.setStyleSheet("font-size: 14px; font-family: Arial; background-color: #E74C3C; color: white; width: 15em; height: 2em;")
        self.layout.addWidget(generate_password_button)

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
        QMessageBox.information(self, "Saved", "Login information saved successfully.")

        # Save data to file
        self.save_data_to_file()

        # Go back to the initial content
        self.show_main_menu()

    def clear_content(self):
        # Clear layout
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

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

        self.result_text.clear()
        self.result_text.insertPlainText("\n".join(passwords))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataManagementSystem()
    window.show()
    sys.exit(app.exec_())
