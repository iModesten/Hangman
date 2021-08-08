offer = input()
menu = {"pizza": ["Margherita", "Four Seasons", "Neapolitan", "Vegetarian", "Spicy"],
        "salad": ["Caesar salad", "Green salad", "Tuna salad", "Fruit salad"],
        "soup": ["Chicken soup", "Ramen", "Tomato soup", "Mushroom cream soup"]}
if offer in menu:
    string_offer = ', '.join(menu[offer])
    print(string_offer)
else:
    print("Sorry, we don't have it in the menu")
