#Import the modules that we'll use
import random
import string

#Enter the length of the password
print("Warning: The password shall be 8-16 characters long.")
length = int(input("\nEnter the desired length of the password: "))

#It will create an unhackable password for your accounts
if length >= 8 and length <= 16:
  lower_case = string.ascii_lowercase
  upper_case = string.ascii_uppercase
  number = string.digits
  symbol = string.punctuation

  create = lower_case + upper_case + number + symbol
  password = "".join(random.sample(create,length))

  print("\nCongratulations! Your password has been created:",password)
else:
  print("\nCan't create a password.")
#Use this password for bank accounts, private documents and mobile wallets
