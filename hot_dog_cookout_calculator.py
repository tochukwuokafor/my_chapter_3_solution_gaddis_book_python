import math
people = int(input('Enter the number of people coming to the cookout: '))
get_hot_dog = int(input('Enter the number of hot dogs each person will be given: '))
HOT_DOG = 10
BUN = 8
dog_required = people * get_hot_dog
dog = dog_required / HOT_DOG
bun = dog_required / BUN
dog_pack = math.floor(dog)
bun_pack = math.floor(bun)
print('The minimum number of packages of hot dogs required is', dog_pack)
print('The minimum number of packages of hot dog buns required is', bun_pack)
if (dog_required % HOT_DOG) > 0:
    print('The number of hot dogs that will be left over is', (dog_required % HOT_DOG))
if (dog_required % BUN) > 0:
    print('The number of hot dog buns that will be left over is', (dog_required % BUN))