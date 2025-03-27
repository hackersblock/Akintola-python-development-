#we can also shorten the code from function3

def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('enter your first name: ')
last_name = input('enter your last name: ')

print('your initials are: ' + get_initial(first_name) \
    + get_initial(last_name))