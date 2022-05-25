print("\t\t:·WELCOME TO BLUE BANK ATM·:\n")
print("\t\tOur new lifestyle requires a new economy")
print("\t\t_________________________________________")
username = input("\n\tEnter your username: ")
password = input("\n\tEnter your password: ")

print(f"\nHello, {username}!")
saved = 100
print(f"\nThe current amount in your account is: ${saved}.")
select = int(input("\nWhat are you doing today? [1-CONTINUE/2-EXIT]: "))

if select == 1:
    print("1-Input Money.")
    print("2-Output Money.")
    print("3-Check my account.")
    print("4-Update my information.")
    cash = int(input("\nSelect what you will do: "))
    if cash == 1:
        plus = float(input("\nAmount to input: $"))
        print(f"The current amount in your account is: ${saved + plus:.2f}.")
    elif cash == 2:
        less = float(input("\nAmount to output: $"))
        if less <= saved:
            print(f"The current amount in your account is: ${saved - less:.2f}")
        else:
            print("You don't have enough money.")
    elif cash == 3:
        print(f"\nThe current amount in your account is: ${saved}")
    elif cash == 4:
        print("\nUpdate ->")
        update = int(input("\n[1-PASSWORD, 2-ADDRESS, 3-CONTACT NUMBER]: "))
        if update == 1:
            print("\nUpdate your password ->")
            key = input("Enter your new password: ")
            print("Your password was succesfully changed.")
        elif update == 2:
            print("\nUpdate your address ->")
            address = input("Enter your new address: ")
            print("Your address was succesfully changed.")
        elif update == 3:
            print("\nUpdate your contact number ->")
            number = input("Enter your new contact number: ")
            print("Your contact number was succesfully changed.")
    else:
        print("\nPlease, select a valid option.")
elif select == 2:
    print(f"\nGoodbye, {username}.")
else:
    print("\nPlease, select a valid option.")
