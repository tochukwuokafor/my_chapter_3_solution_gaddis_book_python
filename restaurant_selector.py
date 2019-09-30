print("Enter 'yes' or 'no'.")
print('--------------------')
vegetarian = input('Is anyone in your party a vegetarian? ')
vegan = input('Is anyone in your party a vegan? ')
gluten_free = input('Is anyone in your party gluten-free? ')
print('Here are your restaurant choices:')
if (vegetarian == 'no') and (vegan == 'no') and (gluten_free == 'no'):
    print("\tJoe's Gourmet Burgers")
if (vegetarian == 'yes') and (vegan == 'no') and (gluten_free == 'yes'):
    print("\tMain Street Pizza Company")
if (vegetarian == 'yes') and (vegan == 'yes') and (gluten_free == 'yes'):
    print("\tCorner Cafe")
    print("\tThe Chef's Kitchen")
if (vegetarian == 'yes') and (vegan == 'no') and (gluten_free == 'no'):
    print("\tMama's Fine Italian")