weight = float(input('Enter the weight of a package: '))

if weight <= 2:
    rate = 1.5
    shipping_charge = weight * rate
    print('The shipping charge is ${:.2f}'.format(shipping_charge))
elif 2 <= weight <= 6:
    rate = 3
    shipping_charge = weight * rate
    print('The shipping charge is ${:.2f}'.format(shipping_charge))
elif 6 <= weight <= 10:
    rate = 4
    shipping_charge = weight * rate
    print('The shipping charge is ${:.2f}'.format(shipping_charge))
elif weight >= 10:
    rate = 4.75
    shipping_charge = weight * rate
    print('The shipping charge is ${:.2f}'.format(shipping_charge))