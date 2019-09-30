print('Reboot the computer and try to connect.')
answer = input('Did that fix the problem? (yes/no) ')
if answer == 'no':
    print('Reboot the router and try to connect.')
    answer = input('Did that fix the problem? (yes/no) ')
    if answer == 'no':
        print('Make sure the cables between the router & modem are plugged in firmly')
        answer = input('Did that fix the problem? (yes/no) ')
        if answer == 'no':
            print('Move the router to a new location and try to connect.')
            answer = input('Did that fix the problem? (yes/no) ')
            if answer == 'no':
                print('Get a new router')
else:
    pass