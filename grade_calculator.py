test_one = int(input('Enter the score for the first test: '))
test_two = int(input('Enter the score for the second test: '))
exam = int(input('Enter the exam score: '))
if not 0 <= test_one <= 25 or not 0 <= test_two <= 25 or not 0 <= exam <= 50:
    print('Error: Enter a valid score!')
else:
    total = test_one + test_two + exam
    print("The student's total score is", total)
    if total < 50 or exam < 25:
        print('Fail!')
    elif total > 80:
        print('Distinction!')
    elif 50 <= total <= 59:
        print('Pass!')
    elif 60 < total < 80:
        print('Credit!')
    elif total < 60:
        print('Pass!')