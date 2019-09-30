year = int(input('Enter a year: '))
if year % 100 == 0:    
    if year % 400 == 0:
        print('In', year, 'February has 29 days')
    else:
        print('Not a leap year')
if year % 100 != 0:
    if year % 4 == 0:
        print('In', year, 'February has 29 days')