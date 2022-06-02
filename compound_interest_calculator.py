print("\t\t\t···································")
print("\t\t\t:··Compound Interest Calculator··:")
print("\t\t\t···································")

print("\nInterest Period:\n")
Pi = {1:'1-Months.',
      2:'2-Years.'}
for value in Pi:
    print(Pi[value])

print("\t\t\t___________________________________")

Pi = int(input("\nChoose an interest period of time: "))

if Pi == 1:
    print("\nYou have chosen to calculate your compound interest monthly.")
    C = float(input("\nEnter your initial investment (USD): "))
    i = float(input("\nEnter your interest rate (%): "))
    n = float(input("\nEnter your interest period of time (months): "))
    Cfinal = C*(1+(i/100))**n
    print(f"\nYou have made an initial investment of {C} USD.")
    print(f"\nYou have chosen an interest rate of {i}%.")
    print(f"\nYou obtain {Cfinal:.2f} USD after {n} months.")
elif Pi == 2:
    print("\nYou have chosen to calculate your compound interest annually.")
    C = float(input("\nEnter your initial investment (USD): "))
    i = float(input("\nEnter your interest rate (%): "))
    n = float(input("\nEnter your interest period of time (years): "))
    Cfinal = C*(1+(i/100))**n
    print(f"\nYou have made an initial investment of {C} USD.")
    print(f"\nYou have chosen an interest rate of {i}%.")
    print(f"\nYou obtain {Cfinal:.2f} USD after {n} years.")
else:
    print("\nERROR: WRONG DATA...")
