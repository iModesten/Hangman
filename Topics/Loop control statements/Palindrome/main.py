word = input()
drow = word[::-1]
for i in range(len(word) // 2):
    if word[i] == drow[i]:
        continue
    else:
        print("Not palindrome")
        break
else:
    print("Palindrome")
