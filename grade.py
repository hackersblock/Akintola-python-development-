#A student makes honour roll if their average is >=85
#and their lowest grade is not below 75
gpa = float(input('what is your grade point average'))
lowest_grade = float(input('what is your lowest grade'))

if gpa >= .85:
    if lowest_grade >= .70:
        print('you made honour roll')