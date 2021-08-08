point_x = float(input())
point_y = float(input())
if point_x > 0 and point_y > 0:
    print('I')
elif point_x < 0 and point_y > 0:
    print('II')
elif point_x < 0 and point_y < 0:
    print('III')
elif point_x > 0 and point_y < 0:
    print('IV')
elif point_x == 0 and point_y == 0:
    print("It's the origin!")
else:
    print("One of the coordinates is equal to zero!")
