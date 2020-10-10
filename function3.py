#when the code looks different but
#have the me logic

#you can also use .upper() in order to get a uppercase respons
#by the code
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('enter your first name: ')
first_name_initial = first_name[0:1].upper()

last_name = input('enter your last name: ')
last_name_initial = last_name[0:1].upper()

print('your initials are: ' + first_name_initial \
    + last_name_initial)