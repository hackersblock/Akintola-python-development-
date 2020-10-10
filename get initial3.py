#the funtion will take a name and return the
#first letter of the name 
#the reason i am using the flase statement and the 
#if and else statement is becausse in a situation where by we are
#  craeting email addresss and we want to be able to have
#  lowcase and uppercase id but only when the user uses them
def get_initial(name, froce_uppercase=True):
    if froce_uppercase:
       initial = name[0:1].upper() 
    else:
        initial = name[0:1]
    return initial

#ask for someones name and return the initials
first_name = input('enter your first name: ')
# first_name_initial = get_initial(first_name,False)
#when we use name notation when pasing a parameter which helps us to be 
#able to write the parameter anyway we chose too
first_name_initial = get_initial(froce_uppercase=False, name=first_name)

print('your initial is: ' + first_name_initial)