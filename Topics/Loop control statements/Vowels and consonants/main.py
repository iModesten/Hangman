vowel_list = ["a", "e", "i", "o", "u"]
sequence = input()
for i in sequence:
    if i.isalpha() and i in vowel_list:
        print("vowel")
    elif i.isalpha():
        print("consonant")
    else:
        break
