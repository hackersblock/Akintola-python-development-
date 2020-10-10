#to get current date and time we need to use the datetime library
from datetime import datetime

current_date = datetime.now()
#the now fuction returns current date nd time as a datetime object

#you must convert the datetime object to a string
#before you convert concatenate it to another string
print('Today is: ' + str(current_date))