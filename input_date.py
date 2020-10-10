from datetime import datetime, timedelta

birthday = input('when is your birthday (dd/mm/yyyy')

birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print ('birthday: ' + str(birthday_date))

one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('day before birthday:' + str(birthday_eve))
