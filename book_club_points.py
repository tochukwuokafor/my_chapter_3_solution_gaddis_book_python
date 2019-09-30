books = int(input('Enter the number of books you purchased this month: '))
LEVEL_ONE = 0
LEVEL_TWO = 5
LEVEL_THREE = 15
LEVEL_FOUR = 30
LEVEL_FIVE = 60
if books == 0:
    print('You earned', LEVEL_ONE, 'points')
elif books == 2:
    print('You earned', LEVEL_TWO, 'points')
elif books == 4:
    print('You earned', LEVEL_THREE, 'points')
elif books == 6:
    print('You earned', LEVEL_FOUR, 'points')
elif books >= 8:
    print('You earned', LEVEL_FIVE, 'points')