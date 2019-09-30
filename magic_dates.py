month = int(input('Enter a month in numeric form: '))
day = int(input('Enter a day in numeric form: '))
year = int(input('Enter a two-digit year: '))
date = month * day
if year == date:
    print('The date is magic!')
else:
    print('Oops! The date is not magic')