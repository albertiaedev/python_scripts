#Use this program to calculate the price to pay for your jewerly
print("Welcome to Jewerler's\nHome of customing jewerly.")

customer = input("\nCustomer: ")
bill = int(input("\nBill Nº: "))

print("\n<")
custom = {1:"·Ring·",2:"·Necklace·",3:"·Brazalet·"}
for value in custom:
    print(custom[value])
custom = int(input(">"))

if custom == 1:
        print("\nDo you want a custom ring?\n")
        ring = {1:'·YES·', 2:'·NO·'}
        for value in ring:
            print(ring[value])
        ring = int(input("\n(1 for YES\n2 for NO)\n>"))
        if ring == 1:
            custom = input("\nEnter your custom word/phrase: ")
            total_price = 200+(len(custom)*10)
            print(f"\nThe total price of your custom ring is = ${total_price:.2f}")
        elif ring == 2:
            total_price = 200
            print(f"\nThe total price of your ring is = ${total_price:.2f}")
        else:
            print("\nPlease, choose a valid option.")
        print(f"\nThank you, {customer}.\nHave a nice day, come back soon!")


elif custom == 2:
        print("\nDo you want a custom necklace?\n")
        necklace = {1:'·YES·', 2:'·NO·'}
        for value in necklace:
            print(necklace[value])
        necklace = int(input("\n(1 for YES\n2 for NO)\n>"))
        if necklace == 1:
            custom = input("\nEnter your custom word/phrase: ")
            total_price = 300+(len(custom)*10)
            print(f"\nThe total price of your custom necklace is = ${total_price:.2f}")
        elif necklace == 2:
            total_price = 300
            print(f"\nThe total price of your necklace is = ${total_price:.2f}")
        else:
            print("\nPlease, choose a valid option.")
        print(f"\nThank you, {customer}.\nHave a nice day, come back soon!")


elif custom == 3:
        print("\nDo you want a custom brazalet?\n")
        brazalet = {1:'·YES·', 2:'·NO·'}
        for value in brazalet:
            print(brazalet[value])
        brazalet = int(input("\n(1 for YES\n2 for NO)\n>"))
        if brazalet == 1:
            custom = input("\nEnter your custom word/phrase: ")
            total_price = 400+(len(custom)*10)
            print(f"\nThe total price of your custom brazalet is = ${total_price:.2f}")
        elif brazalet == 2:
            total_price = 400
            print(f"\nThe total price of your brazalet is = ${total_price:.2f}")
        else:
            print("\nPlease, choose a valid option.")
        print(f"\nThank you, {customer}.\nHave a nice day, come back soon!")

else:
    print("\nPlease, choose a valid option.")
