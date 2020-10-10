#the funtion will take a name and return the
#first letter of the name 
def get_initial(name):
    initial = name[0:1].upper()
    return initial

#ask for someones name and return the initials
first_name = input('enter your first name: ')
first_name_initial = get_initial(first_name)

print('your initiak is: ' + first)