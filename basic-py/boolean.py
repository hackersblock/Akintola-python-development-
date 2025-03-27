#when working with  boolean experssion 
#i check to see if the requirement for honour roll are met
gpa = float(input('what is your garde point average? '))
lowest_grade = float(input('what is your lowest grade? '))

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

#later in your code if you want to check if the student is
#on honour rool, all i need o do us check the boolean variable
#i set earlier in my code
if honour_roll:
    print('you made honour roll')