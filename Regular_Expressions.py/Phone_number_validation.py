import re 
# phone_number='9637642230'   or
phone_number= input("Enter number: ")

pattern = r"^[0-9]{10}$"

if re.match(pattern, phone_number):
    print('Valid number...')
else:
    print('Invalid number...')