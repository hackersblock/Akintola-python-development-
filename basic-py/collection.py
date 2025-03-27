temitope = {}
temitope['first'] = 'temitope'
temitope['last'] = 'akintola'

fola = {}
fola['first'] = 'fola'
fola['last'] = 'akintola'

#always check that it is a [] and not a {}
people = []
people.append(temitope)
people.append(fola)
people.append({
    'first': 'bill', 'last': 'gates'
})

print(people)