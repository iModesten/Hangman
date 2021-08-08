# work with these variables
eugene = set(input().split())
rose = set(input().split())
countries = eugene.symmetric_difference(rose)
print(countries)
