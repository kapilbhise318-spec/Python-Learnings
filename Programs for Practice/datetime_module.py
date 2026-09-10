# import datetime

# today= datetime.datetime.now()
# print(today)

#2 import specific class 

# from datetime import datetime, date, time, timedelta 


# 3 import Everything..

# from datetime import *


from datetime import datetime, date, timedelta

now=datetime.now()
print(now)

# Only today's  date..

today=date.today()
print(today)

# format a date as a string..

print(now.strftime("%d-%m-%Y"))

# parse a string into datetime

dt=datetime.strptime("12-04-2026","%d-%m-%Y")

tomarrow=today+timedelta(days=1)
print(tomarrow)


# diffrence between two days..

d1=date(2026,1,1)
d2=date.today()
diffrence=d1-d2
print(diffrence.days)    #(number of days sinse january.)

