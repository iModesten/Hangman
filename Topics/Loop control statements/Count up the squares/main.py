# put your python code here
sum = 0
squares_sum = 0
while True:
    number = int(input())
    sum += number
    squares_sum += number ** 2
    if number == 0 and sum == 0:
        print(0)
        break
    elif sum == 0:
        print(squares_sum)
        break
