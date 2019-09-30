number = int(input('Enter a number between 1 and 10: '))
roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X'}
if number in roman.keys():
    print(roman[number])
else:
    print('Error: Please enter a number between 1 and 10!')