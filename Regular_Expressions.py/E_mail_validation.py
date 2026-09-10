import re 

# email='kapilbhise318@gail.com'     OR  
email=input('enter your email:  ')

pattern = r"^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$"


if re.match(pattern, email):

    print('Valid email...')

else:

    print('Invalid email...')