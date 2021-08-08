time_point = 10.5
day_hours = 24
offset = int(input())
if time_point + offset < 0:
    print("Monday")
elif 0 <= time_point + offset <= 24:
    print("Tuesday")
elif time_point + offset > 24:
    print("Wednesday")
