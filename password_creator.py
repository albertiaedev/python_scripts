#Import the modules we'll use
import random
import string

#Enter the length of the password
length = int(input("Enter the desired length of the password: "))

#It will create an unhackable password for your accounts
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
number = string.digits
symbol = string.punctuation

create = lower_case + upper_case + number + symbol
password = "".join(random.sample(create,length))

print("\nCongratulations! Your password has been created:",password)
