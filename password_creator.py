#Import the modules we'll use
import random
import string

#Enter the lenght of the password
lenght = int(input("Enter the desired lenght of the password: "))

#It will create an unhackable password for your accounts
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
number = string.digits
symbol = string.punctuation

create = lower_case + upper_case + number + symbol
password = "".join(random.sample(create,lenght))

print("\nCongratulations! Your password has been created:",password)
