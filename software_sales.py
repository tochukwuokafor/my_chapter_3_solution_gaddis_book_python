RETAIL_COST = 99
number = int(input('Enter the number of packages purchased: '))
if 10 <= number <= 19:
    discount = 0.1
    total_cost = number * RETAIL_COST
    discount_amount = discount * total_cost
    final_cost = total_cost - discount_amount
    print('The amount of discount is ${:.2f}'.format(discount_amount))
    print('The total amount of purchase after discount is ${:.2f}'.format(final_cost))
elif 20 <= number <= 49:
    discount = 0.2
    total_cost = number * RETAIL_COST
    discount_amount = discount * total_cost
    final_cost = total_cost - discount_amount
    print('The amount of discount is ${:.2f}'.format(discount_amount))
    print('The total amount of purchase after discount is ${:.2f}'.format(final_cost))
elif 50 <= number <= 99:
    discount = 0.3
    total_cost = number * RETAIL_COST
    discount_amount = discount * total_cost
    final_cost = total_cost - discount_amount
    print('The amount of discount is ${:.2f}'.format(discount_amount))
    print('The total amount of purchase after discount is ${:.2f}'.format(final_cost))
elif number >= 100:
    discount = 0.4
    total_cost = number * RETAIL_COST
    discount_amount = discount * total_cost
    final_cost = total_cost - discount_amount
    print('The amount of discount is ${:.2f}'.format(discount_amount))
    print('The total amount of purchase after discount is ${:.2f}'.format(final_cost))
else:
    print('No discount!')
    print('The total amount of purchase is ${:.2f}'.format(number * RETAIL_COST))  