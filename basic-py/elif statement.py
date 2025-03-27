#working with if and multiply elif statement
province = input('what is your province do you live in')
tax = 0
#working with or statement
# if province in 'akure' or province == 'ibadan':
        #tax = 0.05

#note i had to comment the first code before i could run the second code

#working with 'in statement which allows you to put more the other 3 provinces
if province in ('akure', 'ibadan', 'akoko'):
        tax = 0.05
elif province in 'lagos':
        tax = 0.13
else:
    tax = 0.18
print(tax)