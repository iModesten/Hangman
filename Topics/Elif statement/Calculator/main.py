# put your python code here
first_number = float(input())
second_number = float(input())
operation = input()
if operation == '+':
    print(str(first_number + second_number))
elif operation == '-':
    print(str(first_number - second_number))
elif operation == '/':
    if second_number == 0:
        print('Division by 0!')
    else:
        print(str(first_number / second_number))
elif operation == '*':
    print(str(first_number * second_number))
elif operation == 'mod':
    if second_number == 0:
        print('Division by 0!')
    else:
        print(str(first_number % second_number))
elif operation == 'pow':
    print(str(first_number ** second_number))
elif operation == 'div':
    if second_number == 0:
        print('Division by 0!')
    else:
        print(str(first_number // second_number))
