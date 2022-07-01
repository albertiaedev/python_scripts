#This app tells you what are the right exercises for people your age
name = input("Hi, what's your name? ->")
age = int(input("How old are you? ->"))

print(f"\nHello, {name}. Please enjoy your physical activity.")
print(f"\nYou said you are {age} years old. This is a list of exercises for people your age...")

if age >= 5 and  age <= 18:
    print("\nYou must have at list 60 minutes of physical activity everyday.")
elif age >= 19 and age <= 64:
    print("\nYou must have at least 150 minutes of moderate aerobic activity every week.")
elif age >= 65 and age <= 80:
    print("\nYou must have at least 150 minutes of moderate aerobic activity every week,\nplus strenght exercises twice a week.")
else:
    print("\nWe couldn't find any advice for you.")
