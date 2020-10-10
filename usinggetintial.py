#when the code looks different but
#have the me logic
#this funtion will return the first intial of a name
#ask for someones name and return the initials
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('enter your first name: ')
first_name_initial = get_initial(first_name)

middle_name = input('enter your middle name: ')
middle_name_initial = get_initial(middle_name)

last_name = input('enter your last name: ')
last_name_initial = get_initial(last_name)

print('your initials are: ' + first_name_initial \
    + middle_name_initial + last_name_initial)