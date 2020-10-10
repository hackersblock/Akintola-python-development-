#to get current date anad time we need to use the datetime library
from datetime import datetime 

#the now function rturns current date and time 
today = datetime.now()

#use day, month,year,hour,minute,second functions
# to display only part of the date 
# all these function return integers
# convert them to strings before concatenating them to another strings
print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))
print('hour: ' + str(today.hour))
print('minute: ' + str(today.minute))
print('second: ' + str(today.second))

