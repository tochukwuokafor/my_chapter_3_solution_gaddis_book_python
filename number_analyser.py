number = int(input('Enter an integer: '))
if number > 0:
    print('Positive')
elif number < 0:
    print('Negative')
elif number == 0:
    print('Zero')
if number % 2 == 0:
    print('Even')
else:
    print('Odd')