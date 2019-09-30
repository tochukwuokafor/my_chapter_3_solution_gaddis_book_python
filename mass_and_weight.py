mass = float(input('Enter the mass of the object: '))
weight = mass * 9.8
print('The weight of the object is {:.2f}'.format(weight))
if weight > 500:
    print('The object is too heavy!')
elif weight < 100:
    print('The object is too light!')