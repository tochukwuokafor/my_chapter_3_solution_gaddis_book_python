seconds = int(input('Enter the number of seconds: '))
if 60 <= seconds < 3600:
    minutes = seconds // 60
    seconds = seconds % 60
    print('This is', minutes, 'minutes and', seconds, 'seconds')
elif 3600 <= seconds <= 86400:
    hours = seconds // 3600
    minutes = (seconds - (hours * 3600)) // 60
    seconds = seconds - ((hours * 3600) + (minutes * 60))
    print('This is', hours, 'hours,', minutes, 'minutes, and', seconds, 'seconds')
elif seconds >= 86400:
    days = seconds // 86400
    hours = (seconds - (days * 86400)) // 3600
    minutes = (seconds - ((days * 86400) + (hours * 3600))) // 60
    seconds = seconds - ((days * 86400) + (hours * 3600) + (minutes * 60))
    print('This is', days, 'days,', hours, 'hours,', minutes, 'minutes, and', seconds, 'seconds')