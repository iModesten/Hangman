name = ''
list_name = []
while True:
    name = input()
    if name != '.':
        list_name.append(name)
    else:
        break
print(list_name)
print(len(list_name))
