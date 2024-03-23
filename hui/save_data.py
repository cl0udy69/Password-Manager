def save_address():
    address = input('Street Adress: ')
    state = input('State/province: ')
    city = input('City: ')
    zipcode = input('Zipcode: ')
    aptnumber = input('Apartment Number: ')

    save_address[address] = {'state': state, 'city': city, 'zipcode': zipcode, 'aptnumber': aptnumber}
    
def save_banking():
    bank = input('Bank: ')
    account = input('Account: ')
    routing = input('Routing: ')
    type = input('Account Type: ')
    website = input('Bank Website: ')
    phone_number = input('Phone Number: ')

    save_banking[bank] = {'account': account, 'routing': routing, 'type': type, 'website': website, 'phone number': phone_number}
    
def save_ssn():
    ssn = input('Social Security Number: ')

    save_ssn[ssn] = {'ssn': ssn}
    
def save_phone_number():
    phone = input('Phone Number: ')
    primary = input('Primary Contact: ')
    emergency = input('Emergency Contacts')

    save_phone_number[phone] = {'phone': phone, 'primary': primary, 'emergency': emergency}
    
def save_login():
    domain = input('Domain: ')
    username = input('Username: ')
    password = input('Password: ')
    type = input('Account Type: ')
    name = input('Account Name: ')

    save_login[domain] = {'Username': username, 'Password': password, 'type': type, 'name': name}
    
def save_email():
    email = input('Email: ')
    primary = input('Primary Email: ')
    business = input('Business Email: ')
    preferred = input('Preffered Email for Communication: ')

    save_email[email] = {'email': email, 'primary': primary, 'business': business, 'preferred': preferred}
    
def save_password():
    password = input('Password: ')

    save_password[password] = {'password': password}
    
def save_birth():
    day = input('Day: ')
    month = input('Month: ')
    year = input('Year: ')

    save_birth[day] = {'month': month, 'year': year}
    
def save_gender():
    sex = input('Sex: ')
    gender = input('Gender: ')
    pronouns = input('Pronouns:')
   
    save_gender[sex] = {'sex': sex, 'gender': gender, 'pronouns': pronouns} 
    
def save_nationality():
    nationality = input('Country: ')
    citizenship = input('Country of Citizenship: ')
    origin = input('National Origin: ')
    
    save_nationality[nationality] = {'nationality': nationality, 'citizenship': citizenship, 'origin': origin,}
    
def save_occupation():
    title = input('Job Title: ')
    company = input('Company: ')
    profession = input('Profession: ')
    years_of_experience = input('Years of Experience: ')
    
    save_occupation[title] = {'title': title, 'company': company, 'profession': profession, 'years of experience': years_of_experience}
    
def save_education():
    level = input('Highest level of education: ')
    degree = input('Highest degree earned: ')
    field = input('Field of Study: ')
    
    save_education[level] = {'level': level, 'degree': degree, 'field': field}
    
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
    
def save_insurance():
    name = input('Insurance company name: ')
    policy = input('Insurance policy number: ')
    number = input('Insurance group number: ')
    plan = input('Insurance plan type: ')
    effective_date = input('Insurance plan effective date: ')
    expiration_date = input('Insurance plan expiration date: ')
    detail = input('Insurance plan coverage details: ')
    insured = input('Assets Insured: ')
    deductible = input('Insurance plans deductible amount: ')
    co_payment = input('Insurance plans co-pay amount: ')
    
    save_insurance[name] = {'policy': policy, 'number': number, 'plan': plan, 'effective date': effective_date, 'expiration date': expiration_date, 'detail': detail, 'insured': insured, 'deductible': deductible, 'co-payment': co_payment}
    
def save_passport():
    number = input('Passport number: ')
    date = input('Date of Issue: ')
    expiration = input('Date of Expiration: ')
    country = input('Issuing Country: ')
    place = input('Place of Issue: ')
    name = input('Full Name: ')
    dob = input('Date of Birth: ')
    gender = input('Gender: ')
    nationality = input('Nationality: ')
    restrictions = input('Restrictions or Limitations: ')
    
    save_passport[number] = {'number': number, 'date': date, 'expiration': expiration, 'country': country, 'place': place, 'name': name, 'dob': dob, 'gender': gender, 'nationality': nationality, 'restrictions': restrictions}
    
def save_legal():
    issues = input('Legal Issues: ')
    obligations = input('Legal Obligations or Restrictions: ')
    documents = input('legal Documents: ')
    
    save_legal[issues] = {'issues': issues, 'obligations': obligations, 'documents': documents}
    
def save_ethnicity():
    ethnicity = input('Ethnicity: ')
    racial = input('Racial Background: ')
    cultural = input('Cultural Background: ')
    
    save_ethnicity[ethnicity] = {'ethnicity': ethnicity, 'racial': racial, 'cultural': cultural}