coordinate_one = int(input())
coordinate_two = int(input())
if 2 <= coordinate_one <= 7 and 2 <= coordinate_two <= 7:
    print(8)
elif (coordinate_one == 1 and coordinate_two == 8) or (coordinate_one == 8 and coordinate_two == 1) or (coordinate_one == 1 and coordinate_two == 1) or (coordinate_one == 8 and coordinate_two == 8):
    print(3)
elif coordinate_one == 1 or coordinate_two == 1 or coordinate_one == 8 or coordinate_two == 8:
    print(5)
