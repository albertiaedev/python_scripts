#Record the sale of a book
print("Welcome to our bookstore.")
print("This is the book we have for you:\n")

client = input("Name of the client: ")
bill = int(input("Bill Nº: "))

print(f'\nHi, {client}. Have a nice day. You checked the bill nº {bill}.\n')

class Book:
    def __init__(self):
        self.title = input("Title: ")
        self.quantity = int(input("Quantity: "))
        self.author = input("Author: ")
        self.price = float(input("Price: $"))

    def books(self):
        print("\nYour book:\n")
        print(f"Title: {self.title}")
        print(f"Quantity: {self.quantity}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")

new_book = Book()
new_book.books()

print("\nThanks for joining us and enjoy your purchase.\
            \nCome back soon!")
