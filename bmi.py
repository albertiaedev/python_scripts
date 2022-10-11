#Get to know your body mass index

print(":BMI Calculator:")

try:
    weight = float(input("\nEnter your weight (kg): "))
    height = float(input("\nEnter your height (m): "))
    bmi = weight / height ** 2

    print(f"\nYour BMI is: {bmi:.2f}")

    if bmi >= 16 and bmi <= 18.4:
        print("\nYour current weight is under the regular value for your height.")
    elif bmi >= 18.5 and bmi <= 24.9:
        print("\nYour current weight is a normal value for your height.")
    elif bmi >= 25 and bmi <= 50:
        print("\nYour current weight is over the regular value for your height.")
    else:
        print("\nThis BMI doesn't seem correct.")
        print("\nPlease, try again.")
except:
    print("\nPlease, enter a valid value.")
