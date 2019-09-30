weight = float(input('Enter your weight (in pounds): '))
height = float(input('Enter your height (in inches): '))
bmi = weight * (703 / (height ** 2))
if 18.5 <= bmi <= 25:
    print('Optimal Weight!')
elif bmi < 18.5:
    print('Underweight!')
elif bmi > 25:
    print('Overweight!')