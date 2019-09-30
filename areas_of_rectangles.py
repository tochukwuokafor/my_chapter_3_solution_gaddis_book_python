NUMBER_RECTANGLES = 2
areas = []
for idx in range(NUMBER_RECTANGLES):
    print('Enter the length of rectangle #', idx + 1, ' : ', sep = '', end = '')
    length = float(input())
    print('Enter the width of rectangle #', idx + 1, ' : ', sep = '', end = '')
    width = float(input())
    area_rectangle = length * width
    areas.append(area_rectangle)
if areas[0] > areas[1]:
    print('The first rectangle has a greater area.')
elif areas[0] < areas[1]:
    print('The second rectangle has a greater area.')
else:
    print('Both rectangles have equal area')