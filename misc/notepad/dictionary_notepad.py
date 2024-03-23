class PersonalInformationManager:
    def __init__(self):
        self.user_choices = {
            'address_choices': ['1', 'one', 'One', 'Address Information', 'Address information', 'address information', 'Address Info', 'Address info', 'address info', 'Address', 'address'],
            'banking_choices': ['2', 'two', 'Two', 'Banking Information', 'Banking information', 'banking information', 'Bank Information', 'Banking information', 'banking information', 'Banking Info', 'Banking info', 'banking info', 'Bank Info', 'Bank info', 'bank info'],
            'ssn_choices': ['3', 'three', 'Three', 'Social Security Number Information', 'Social security number information', 'social security number information', 'Social Security Information', 'Social security information', 'social security information', 'Social Security Number Info', 'Social security number info', 'social security number info', 'Social Securtiy Info', 'Social security info', 'social security info', 'SSN Information', 'SSN information', 'ssn information', 'SSN Info', 'SSN info', 'ssn info', 'Social Security Number', 'Social security number', 'social security number', 'Social Security', 'Social security', 'social security', 'SSN', 'ssn'],
            'phone_number_choices': ['4', 'four', 'Four', 'Phone Number Information', 'Phone number information', 'phone number information', 'Phone Number Info', 'Phone number info', 'phone number info', 'Phone Number', 'Phone number', 'phone number'],
            'login_choices': ['5', 'five', 'Five', 'Login Information', 'Login information', 'login information', 'Login Info', 'Login info', 'login infop', 'Login', 'login'],
            'email_choices': ['6', 'six', 'Six', 'Email Information', 'Email information', 'email information', 'Email Info', 'Email info', 'email info', 'Email', 'email'],
            'password_choices': ['7', 'seven', 'Seven', 'Password', 'password', 'Password Information', 'Password information', 'password information', 'Password Info', 'Password info', 'password info'],
            'birth_choices': ['', 'Birthday Information', 'Birthday information', 'birthday information', 'Birthday Info', 'Birthday info', 'birthday info', 'Birthday', 'birthday', 'Date of Birth', 'Date of birth', 'date of birth', 'Birth', 'birth'],
            'gender_choices': ['', 'Gender Information', 'Gender information', 'gender information', 'Gender Info', 'Gender info', 'gender info', 'Gender', 'gender'],
            'nationality_choices': ['', 'Nationality Information', 'Nationality information', 'nationality information', 'Nationality Info', 'Nationality info', 'nationality info', 'Nationality', 'nationality'],
            'occupation_choices': ['', 'Occupation Information', 'Occupation information', 'occupation information', 'Occupation Info', 'Occupation info', 'occupation info', 'Job Information', 'Job information', 'job information', 'Job Info', 'Job info', 'job info', 'Occupation', 'occupation', 'Job', 'job'],
            'education_choices': ['', 'Education Information', 'Education information', 'education information', 'Education Info', 'Education info', 'education info', 'Education', 'education'],
            'medical_choices': ['', 'Medical Information', 'Medical information', 'medical information', 'Medical Info', 'Medical info', 'medical info', 'Medical', 'medical'],
            'insurance_choices': ['', 'Insurance Information', 'Insurance information', 'insurance information', 'Insurance Info', 'Insurance info', 'insurance info', 'Insurance', 'insurance'],
            'driving_choices': ['', 'Drivers License', 'Drivers license', 'drivers license', 'Driving Information', 'Driving information', 'driving information', 'Driving Info', 'Driving info', 'driving info', 'Driving', 'driving'],
            'passport_choices': ['', 'Passport Information', 'Passport information', 'passport information', 'Passport Info', 'Passport info', 'passport info', 'Passport', 'passport'],
            'legal_choices': ['', 'Legal Information', 'Legal information', 'legal information', 'Legal Info', 'Legal info', 'legal info', 'Legal', 'legal'],
            'ethnicity_choices': ['', 'Ethnicity Information', 'Ethnicity information', 'ethnicity information', 'Ethnicity Info', 'Ethnicity info', 'ethnicity info', 'Ethnicity', 'ethnicity'],
            'save_address_choices': ['1', 'one', 'One', 'Save', 'save', 'Save Address', 'Save address', 'save address', 'Save Billing Address', 'Save billing address', 'save billing address'],
            'save_banking_choices': ['1', 'one', 'One', 'Save', 'save', 'Save Banking Information', 'Save banking information', 'save banking information', 'Save Banking Info', 'Save banking info', 'save banking info'],
            'save_ssn_choices': ['1', 'one', 'One', 'Save', 'save', 'Save Social Security Number', 'Save social security number', 'save social security number', 'Save Social Security', 'Save social security', 'save social security', 'Save SSN', 'Save ssn', 'save SSN', 'save ssn'],
            'save_phone_number_choices': ['1', 'one', 'Save', 'save', 'One', 'Save Phone Number', 'Save phone number', 'save phone number', 'Save Number', 'Save number', 'save number'],
            'save_login_choices': ['1', 'one', 'One', 'Save', 'save', 'Save Login', 'Save login', 'save login'],
            'save_email_choices': ['1', 'one', 'One', 'Save', 'save', 'Save Email', 'Save email', 'save email'],
            'save_password_choices': ['1', 'one', 'One', 'Save', 'save', 'Save Password', 'Save password', 'save password'],
            'save_birth_choices': ['1', 'one', 'One', 'Save', 'save', 'Save Birthday', 'Save birthday', 'save birthday', 'Save Date of Birth', 'Save date of birth', 'save date of birth'],
            'save_gender_choices': ['1', 'one', 'One', 'Save', 'save', 'Save Gender', 'Save gender', 'save gender'],
            'save_nationality_choices': ['1', 'one', 'One', 'Save', 'save', 'Save Nationality', 'Save nationality', 'save nationality'],
            'save_occupation_choices': ['1', 'one', 'One', 'Save', 'save', 'Save Occupation', 'Save occupation', 'save occupation', 'Save Job', 'Save job', 'save job'],
            'save_education_choices': ['1', 'one', 'One', 'Save', 'save', 'Save Education', 'Save education', 'save education'],
            'save_medical_choices': ['1', 'one', 'One', 'Save', 'save', 'Save Medical', 'Save medical', 'save medical'],
            'save_insurance_choices': ['1', 'one', 'One', 'Save', 'save', 'Save Insurance', 'Save insurance', 'save insurance'],
            'save_driving_choices': ['1', 'one', 'One', 'Save', 'save', 'Save Driving', 'Save driving', 'save driving'],
            'save_passport_choices': ['1', 'one', 'One', 'Save', 'save', 'Save Passport', 'Save passport', 'save passport'],
            'save_legal_choices': ['1', 'one', 'One', 'Save', 'save', 'Save Legal', 'Save legal', 'save legal'],
            'save_ethnicity_choices': ['1', 'one', 'One', 'Save', 'save', 'Save Ethnicity', 'Save ethnicity', 'save ethnicity'],
        }

    def get_choice(self, user_input):
        for key, value in self.user_choices.items():
            if user_input in value:
                return key
        return None

    def save_choice(self, user_input):
        save_choices = {
            'address_choices': ['Address Information'],
            'banking_choices': ['Banking Information'],
            'ssn_choices': ['Social Security Number Information'],
            'phone_number_choices': ['Phone Number Information'],
            'login_choices': ['Login Information'],
            'email_choices': ['Email Information'],
            'password_choices': ['Password Information'],
            'birth_choices': ['Birthday Information'],
            'gender_choices': ['Gender Information'],
            'nationality_choices': ['Nationality Information'],
            'occupation_choices': ['Occupation Information'],
            'education_choices': ['Education Information'],
            'medical_choices': ['Medical Information'],
            'insurance_choices': ['Insurance Information'],
            'driving_choices': ['Driving Information'],
            'passport_choices': ['Passport Information'],
            'legal_choices': ['Legal Information'],
            'ethnicity_choices': ['Ethnicity Information'],
        }

        for key, value in save_choices.items():
            if user_input in value:
                return key
        return None


pim = PersonalInformationManager()

user_input = input("Enter your choice: ")

choice = pim.get_choice(user_input)
if choice:
    print("Your choice is:", choice)
else:
    print("Invalid choice")

save_input = input("Enter your save choice: ")

save_choice = pim.save_choice(save_input)
if save_choice:
    print("Your save choice is:", save_choice)
else:
    print("Invalid save choice")
