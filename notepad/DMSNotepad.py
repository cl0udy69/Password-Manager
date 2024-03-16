def personal_information_selection():
  address_choices = ['1', 'one', 'One', 'Address', 'Address\'s', 'address', 'address\'s']
  banking_choices = ['2', 'two', 'Two', 'Banking Information', 'Banking information', 'banking information', 'Bank Information', 'Banking information', 'banking information', 'Banking Info', 'Banking info', 'banking info', 'Bank Info', 'Bank info', 'bank info']
  ssn_choices = ['3', 'three', 'Three', 'Social Security Number', 'Social security number', 'social security number', 'Social Security', 'Social security', 'social security', 'SSN', 'ssn']
  phone_number_choices = ['4', 'four', 'Four', 'Phone Number', 'Phone number', 'phone number']

  personal_information = input ('Choose one of the following options ')
  print('Address\'s')
  print('Banking Information')
  print('Social Security Number')
  print('Phone Number')

  if personal_information == address_choices:
      address_selection()
  if personal_information == banking_choices:
      banking_selection()  
  if personal_information == ssn_choices:
      ssn_selection()
  if personal_information == phone_number_choices:
      phone_number_selection()

def address_selection():
  save_address_choices = ['1', 'one', 'One', 'Save Address', 'Save address', 'save address', 'Save Billing Address', 'Save billing address', 'save billing address']
  see_address_choices = ['2', 'two', 'Two', 'See Saved Address', 'See saved address', 'see saved address', 'See Address', 'See address', 'see address', 'View Saved Address', 'View saved address', 'view saved address', 'View Address', 'View address', 'view address']

  selection = input('Would you like to saved view address\'s or save an address.')
  if selection == save_address_choices:
      address_saver()
  if selection == see_address_choices:
      see_saved_address()

def banking_selection():
  save_banking_choices = ['1', 'one', 'One', 'Save Banking Information', 'Save banking information', 'save banking information', 'Save Banking Info', 'Save banking info', 'save banking info']
  see_banking_choices = ['2', 'two', 'Two', 'See saved banking information', 'see saved banking information', 'See saved banking info', 'see saved banking info', 'See Banking Information', 'See banking information', 'See Banking Info', 'See banking info', 'see banking info', 'View saved banking information', 'view saved banking information', 'View saved banking info', 'view saved banking info', 'View Banking Information', 'View banking information', 'View Banking Info', 'View banking info', 'view banking info']

  selection = input('Would you like to save your banking information, or view saved information')
  if selection == save_banking_choices:
      bank_saver()
  if selection == see_banking_choices:
      see_saved_banking_info()

def ssn_selection():
  save_ssn_choices = ['1', 'one', 'One', 'Save Social Security Number', 'Save social security number', 'save social security number', 'Save Social Security', 'Save social security', 'save social security', 'Save SSN', 'Save ssn', 'save SSN', 'save ssn']
  see_ssn_choices = ['2', 'two', 'Two', 'See saved social security number', 'see saved social security number', 'See saved social security', 'see saved social security', 'See saved SSN', 'See saved ssn', 'See saved ssn', 'see saved ssn', 'see saved SSN', 'See social security number', 'see saved security number', 'See social security', 'see social security', 'See SSN', 'see SSN', 'See ssn', 'see ssn', 'View saved social security number', 'view saved social security number', 'View saved social security', 'sview saved social security', 'View saved SSN', 'View saved ssn', 'View saved ssn', 'view saved ssn', 'view saved SSN', 'View social security number', 'view saved security number', 'View social security', 'view social security', 'View SSN', 'view SSN', 'View ssn', 'view ssn']

  selection = input('Would you like to save your social security number or view saved information')
  if selection == save_ssn_choices:
      ssn_saver()
  if selection == see_ssn_choices:
      see_saved_ssn()

def phone_number_selection():
  save_phone_number_choices = ['1', 'one', 'One', 'Save Phone Number', 'Save phone number', 'save phone number', 'Save Number', 'Save number', 'save number']
  see_phone_number_choices = ['2', 'two', 'Two', 'See Saved Phone Number', 'See saved phone number', 'see saved phone number', 'See Phone Number', 'See phone number', 'see phone number', 'See Saved Number', 'See saved number', 'see saved number', 'See Number', 'See number', 'see number']

  selection = input('Would you like to save a phone number or see view saved information')
  if selection == save_phone_number_choices:
      phone_number_saver()
  if selection == see_phone_number_choices:
      see_saved_phone_number()
