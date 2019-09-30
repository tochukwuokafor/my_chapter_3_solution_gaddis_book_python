month_number = int(input('Enter a month number between 1 and 12: '))
if month_number in [1, 2, 3]:
    print('The month is in first quarter.')
elif month_number in [4, 5, 6]:
    print('The month is in second quarter.')
elif month_number in [7, 8, 9]:
    print('The month is in third quarter.')
elif month_number in [10, 11, 12]:
    print('The month is in fourth quarter')
else:
    print('Error: Enter a month number between 1 and 12!')