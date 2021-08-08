# put your python code here
number = 0
while True:
    number = int(input())
    if number > 100:
        break
    elif number < 10:
        continue
    else:
        print(str(number))
