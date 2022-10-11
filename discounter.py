#Calculate the discount percentage for your products

print(":Discount Calculator:")

select = input("\nProduct name: ")
price = float(input("\nOriginal price: "))
discount = float(input("\nDiscount (%): "))

print(f"\nYou have to pay: \
{price - (price * (discount / 100)):.2f}")

print(f"\nYou save in this purchase: \
{price * (discount / 100):.2f}")
