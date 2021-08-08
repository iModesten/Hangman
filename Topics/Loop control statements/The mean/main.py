list_numbers = []
while True:
    number = input()
    if number != '.':
        list_numbers.append(int(number))
    else:
        print(sum(list_numbers) / len(list_numbers))
        break
