print("|:WELCOME:|")
print("\nBackend Calculator\n")
name=input("Name: ")
print("\nOptions ->\n")

option={1:"1.Add.",2:"2.Rest.",
        3:"3.Multiply.",4:"4.Divide."}
for value in option:
    print(option[value])
option=int(input(f"\nHello, {name}. Choose the operation you will do: "))

num=int(input("\nHow many numbers you will choose?: "))

#Operation with 2 numbers
if num == 2:
    if option >= 1 or option <= 4:
        print("\nPick your numbers:")
    else:
        print("\nCan't do any operation.")
        
    num1=float(input("->"))
    num2=float(input("->"))

    if option == 1:
        result=num1+num2
        print(f"\nYour result -> {num1} + {num2} = {result:.2f}")
    elif option == 2:
        result=num1-num2
        print(f"\nYour result -> {num1} - {num2} = {result:.2f}")
    elif option == 3:
        result=num1*num2
        print(f"\nYour result -> {num1} x {num2} = {result:.2f}")
    elif option == 4:
        result=num1/num2
        print(f"\nYour result -> {num1} / {num2} = {result:.2f}")

#Operation with 3 numbers
elif num == 3:
    if option >= 1 or option <= 4:
        print("\nPick your numbers:")
    else:
        print("\nCan't do any operation.")
        
    num1=float(input("->"))
    num2=float(input("->"))
    num3=float(input("->"))

    if option == 1:
        result=num1+num2+num3
        print(f"\nYour result -> {num1} + {num2} + {num3} = {result:.2f}")
    elif option == 2:
        result=num1-num2-num3
        print(f"\nYour result -> {num1} - {num2} - {num3} = {result:.2f}")
    elif option == 3:
        result=num1*num2*num3
        print(f"\nYour result -> {num1} x {num2} x {num3} = {result:.2f}")
    elif option == 4:
        result=num1/num2/num3
        print(f"\nYour result -> {num1} / {num2} / {num3} = {result:.2f}")

#Operation with 4 numbers
elif num == 4:
    if option >= 1 or option <= 4:
        print("\nPick your numbers:")
    else:
        print("\nCan't do any operation.")
        
    num1=float(input("->"))
    num2=float(input("->"))
    num3=float(input("->"))
    num4=float(input("->"))

    if option == 1:
        result=num1+num2+num3+num4
        print(f"\nYour result -> {num1} + {num2} + {num3} + {num4} = {result:.2f}")
    elif option == 2:
        result=num1-num2-num3-num4
        print(f"\nYour result -> {num1} - {num2} - {num3} - {num4} = {result:.2f}")
    elif option == 3:
        result=num1*num2*num3*num4
        print(f"\nYour result -> {num1} x {num2} x {num3} x {num4} = {result:.2f}")
    elif option == 4:
        result=num1/num2/num3/num4
        print(f"\nYour result -> {num1} / {num2} / {num3} / {num4} = {result:.2f}")

#Non-valid operation
else:
    print("\nCan't do any operation.")
    
print(f"\nThat was it all for now, {name}.")
print("\nHope to see you soon.")
print("\nGoodbye!") 
