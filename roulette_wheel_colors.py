pocket_number = int(input('Enter a pocket number: '))
POCKETS = 36
if pocket_number not in range(POCKETS + 1):
    print('Error: Enter a valid pocket number!')
else:
    if pocket_number == 0:
        print('Green!')
    elif 1 <= pocket_number <= 10:
        if pocket_number % 2 == 0:
            print('Black!')
        else:
            print('Red!')
    elif 11 <= pocket_number <= 18:
        if pocket_number % 2 == 0:
            print('Red!')
        else:
            print('Black!')
    elif 19 <= pocket_number <= 28:
        if pocket_number % 2 == 0:
            print('Black!')
        else:
            print('Red!')
    elif 29 <= pocket_number <= 36:
        if pocket_number % 2 == 0:
            print('Red!')
        else:
            print('Black!')