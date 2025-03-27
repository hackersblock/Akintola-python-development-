#code calculate the amount of tax you paying for a goods on a website

country = input('what country are you from')

#the reason i wrote .lower () is because i dont want it to be case sensitive
if country.lower () == 'nigeria':
    province = input('what is your province')
    if province in ('akure', 'ibadan', 'akoko') :
            tax = 0.05
    elif province == 'lagos':
            tax = 0.13
    else:
            tax = 0.15
else:
    tax = 0.26
print(tax)