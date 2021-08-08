list_numbers = []
while True:
    number = input()
    if number != '.':
        list_numbers.append(float(number))
    else:
        print(min(list_numbers))
        break
