#Calculate your salary per hour
print("~~~~~~~~~~~~~~~~~~")
print("| SysPython LLC |")
print("~~~~~~~~~~~~~~~~~~")

print("\nPython LLC")

var1 = input("\nEnter your first name: ")
var2 = input("\nEnter your last name: ")
var3 = input("\nEnter your ID: ")

print(f"\nWelcome to SysPython LLC, {var1} {var2}")

var4 = int(input("\nEnter your Personal Access Code (0-40): "))

if var4 >= 0 and var4 <= 9:
    print("\nYou belong to group #1.")
    if var4 <= 4:
        print("\nYou're currently earning $8.00 per hour.")
    elif var4 >= 4 and var4 <= 9:
        print("\nYou're currently earning $8.50 per hour.")
elif var4 >= 10 and var4 <=19:
    print("\nYou belong to group #2.")
    if var4 >= 10 and var4 <= 14:
        print("\nYou're currently earning $9.00 per hour.")
    elif var4 >= 15 and var4 <=19:
        print("\nYou're currently earning $9.50 per hour.")
elif var4 >= 20 and var4 <= 29:
    print("\nYou belong to group #3.")
    if var4 >= 20 and var4 <= 24:
        print("\nYou're currently earning $10.00 per hour.")
    elif var4 >= 25 and var4 <=29:
        print("\nYou're currently earning $10.75 per hour.")
elif var4 >= 30 and var4 <= 40:
    print("\nYou belong to group #4.")
    if var4 >= 30 and var4 <= 34:
        print("\nYou're currently earning $11.00 per hour.")
    elif var4 >= 35 and var4 <=40:
        print("\nYou're currently earning $12.00 per hour.")
else:
    print("\nYour selection exceeds the number of workers of this company.")

print("\nThank you for being a member of Python LLC!")
print("\nFor further information, contact (+58) 243 xxxxxxx.")
