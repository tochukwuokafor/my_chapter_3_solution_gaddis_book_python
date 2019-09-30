penny = int(input('Enter the number of pennies: '))
nickel = int(input('Enter the number of nickels: '))
dime = int(input('Enter the number of dimes: '))
quarters = int(input('Enter the number of quarters: '))
PENNIES = 100
NICKELS = 20
DIMES = 10
QUARTERS = 4
dollar = (penny / PENNIES) + (nickel / NICKELS) + (dime / DIMES) + (quarters / QUARTERS)
if dollar == 1:
    print("Congratulations! You've entered one dollar!")
elif dollar > 1:
    print("Sorry! You've entered more than one dollar")
else:
    print("Sorry! You've entered less than one dollar")