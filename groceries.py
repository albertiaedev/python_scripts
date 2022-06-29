#Make a grocery list or you can also use it in stock control
print("\tSUPERMARKET LIST\n")
name = input("Who's the owner of this list?\nYour name: ")

add = input("\nDo you want to add an item?\nY/N-> ")

if add == 'Y'.lower():
        items = []
        i = 0
        while 1:
            i+=1
            item = input('\nAdd a new item - Item#%d: '%i)
            if item == '':
                break
            items.append(item)
        print('\n',items)
        note = input("\nActivate notifications\nY/N-> ")
        if note == 'Y'.lower():
                print("\nNotifications on.")
                print("\nRemember to buy your groceries...")
        elif note == 'N'.lower():
                print("\nNotifications off.")
        else:
                print("\nYour notifications were turned off automatically.")
elif add == 'N'.lower():
        print(f"\nThat's it for now, {name}.")
        print("\nHave a nice day!")
        note = input("\nActivate notifications\nY/N-> ")
        if note == 'Y'.lower():
                print("\nNotifications on.")
                print("\nRemember to buy your groceries...")
        elif note == 'N'.lower():
                print("\nNotifications off.")
        else:
                print("\nYour notifications were turned off automatically.")
else:
        print("\nAn error has occurred.")
