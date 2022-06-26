#Input your grades to calculate the averageto check if you pass
#or fail the semester
print("FINAL AVERAGE GRADES CALCULATOR")
print("\nWelcome.")
print("\nPlease, verify your grades in order to know your average.")

var1 = input("\nEnter your first name: ")
var2 = input("\nEnter your last name: ")
var3 = input("\nEnter your ID: ")

print(f"\nHello, {var1}. Let's calculate your grades.\n")

math = float(input("Enter your final grade for 'Math': "))
phy = float(input("Enter your final grade for 'Physics': "))
chem = float(input("Enter your final grade for 'Chemistry': "))
bio = float(input("Enter your final grade for 'Biology': "))
geo = float(input("Enter your final grade for 'Geography': "))
hist = float(input("Enter your final grade for 'History': "))
art = float(input("Enter your final grade for 'Arts': "))
eng = float(input("Enter your final grade for 'English': "))

avg = (math + phy + chem + bio + geo + hist + art + eng) / 8

print(f"\nThank you, {var1}. We've done your grades")
show = int(input("\n[Press '1' + 'Enter' to show] / [Press '2' + 'Enter' to exit] -> "))

if show == 1:
    if avg >= 6 and avg <=10:
        print(f"\nWell, {var1}. We got news for you ->\n")
        print(f"Congratulations, {var1} {var2}. YOU HAVE PASSED.")
        print(f"Your average grade has been: {avg:.2f}/10")
        print("\nSee you on the next period.")
    elif avg > 10:
        print("\nAn error has ocurred...")
        print("The average grade shall not be over 10.")
    elif avg < 0:
        print("\nAn error has ocurred...")
        print("The average grade shall not be a negative number.")
    else:
        print(f"\nWell, {var1}. We got news for you ->\n")
        print(f"We're sorry, {var1} {var2}. YOU HAVE FAILED.")
        print(f"Your average grade has been: {avg:.2f}/10")
        print("\nSee you on the next period.")
elif show == 2:
    print("\nThat's it for now...")
    print(f"\nBye, {var1}. We'll be glad to see you on the next period.")
else:
    print("\nAn error has ocurred...")
    print("\nPlease, start the process again.")

print("\nThank you for choosing our institute for your studies.")
