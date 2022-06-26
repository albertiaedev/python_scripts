#Choose a color for your brand logo
print("|:·:·PICK-A-PSYCOLOR·:·:|")

print("\nWelcome!\n\nChoose a color that relates to an attribute according to psychology:\n")
color={1:'1. Red.',2:'2. Blue.',3:'3. Green.',4:'4. Yellow.',5:'5. Orange.',
       6:'6. Purple.',7:'7. Pink.',8:'8. Brown.',9:'9. White.',10:'10. Black.'}
for value in color:
    print(color[value])
color=int(input("\nSelect the number of your color: "))

if color == 1:
    print("\nThe color 'Red' is related to the following attributes:\n")
    att=['·Passion.','·Energy.','·Heat.','·Dinamism.']
    for x in att:
        print(x)
    print("\nIt's usually used for: Transportation, Technology & Food.")
elif color == 2:
    print("\nThe color 'Blue' is related to the following attributes:\n")
    att=['·Calm.','·Honesty.','·Professionality.','·Compromise.']
    for x in att:
        print(x)
    print("\nIt's usually used for: Technology, Healthcare & Finance.")
elif color == 3:
    print("\nThe color 'Green' is related to the following attributes:\n")
    att=['·Nature.','·Ethics.','·Growth.','·Organic.']
    for x in att:
        print(x)
    print("\nIt's usually used for: Natural Resources, Energy & Food.")
elif color == 4:
    print("\nThe color 'Yellow' is related to the following attributes:\n")
    att=['·Joy.','·Positive.','·Kindness.','·Brightness.']
    for x in att:
        print(x)
    print("\nIt's usually used for: Energy, Household & Food.")
elif color == 5:
    print("\nThe color 'Orange' is related to the following attributes:\n")
    att=['·Youth.','·Fun.','·Modern.','·Innovation.']
    for x in att:
        print(x)
    print("\nIt's usually used for: Energy, Food & Natural Resources.")
elif color == 6:
    print("\nThe color 'Purple' is related to the following attributes:\n")
    att=['·Luxury.','·Wisdom.','·Dignity.','·Mistery.']
    for x in att:
        print(x)
    print("\nIt's usually used for: Clothes, Technology & Airlines.")
elif color == 7:
    print("\nThe color 'Pink' is related to the following attributes:\n")
    att=['·Female.','·Fun.','·Tenderness.','·Romance.']
    for x in att:
        print(x)
    print("\nIt's usually used for: Women Products, Clothes & Food.")
elif color == 8:
    print("\nThe color 'Brown' is related to the following attributes:\n")
    att=['·Male.','·Earth.','·Rural.','·Simple.']
    for x in att:
        print(x)
    print("\nIt's usually used for: Men Products, Clothes & Natural Resources.")
elif color == 9:
    print("\nThe color 'White' is related to the following attributes:\n")
    att=['·Purity.','·Neatness.','·Nobleness.','·Naiveness.']
    for x in att:
        print(x)
    print("\nIt's usually used for: Household, Healthcare & Technology.")
elif color == 10:
    print("\nThe color 'Black' is related to the following attributes:\n")
    att=['·Value.','·Prestige.','·Power.','·Death.']
    for x in att:
        print(x)
    print("\nIt's usually used for: Technology, Clothes & Real Estate.")
else:
    print("\nYour choice isn't available...")

print("\nThank you for using PICK-A-PSYCOLOR.")
print("\nHopefully, this will help you choose a color for your brand.")
 
