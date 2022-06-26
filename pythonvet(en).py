#Vet clinical history
print("\t\t\t:·PYTHON-VET by J.A. Hernández·:")
print("\n:·Our goal is to offer to you the best experience for veterinary assistance·:")
print("_____________________________________________________________________________")

var1 = input("\nName of veterinary: ")
var2 = input("\nName of owner: ")
var3 = input("\nName of patient: ")

print(f"\nWelcome to consultation, Doctor {var1}.")
print(f"\nYou are assisting today to: {var2} and his/her pet {var3}.")

print(f"\nLet's update {var3}'s clinical history.")
var4 = input(f"\nDoes {var3} come for a medical control or it's its first consultation?: ")
print(f"\nAlright! We will help {var3} throughout its {var4}.")
    
    # The species available for consultation are shown in the menu of species

print("\n:Menu of species:\n")
menu = {1:"1. Dog", 2:"2. Cat", 3:"3. Mammal",
        4:"4. Bird", 5:"5. Reptile"}
for value in menu:
    print(menu[value])
menu = int(input("\nEnter the kind of patient for consultation: "))

try:
    if menu == 1:
        print("\nYour selection: Dog")
        var5 = input("\nEnter your patient's breed: ")
        print(f"\nYour patient called {var3} is a dog and its breed is {var5}.")
    elif menu == 2:
        print("\nYour selection: Cat")
        var5 = input("\nEnter your patient's breed: ")
        print(f"\nYour patient called {var3} is a cat and its breed is {var5}.")
    elif menu == 3:
        print("\nYour selection: Mammal")
        var6 = input("\nEnter your patient's species: ")
        print(f"\nYour patient called {var3} is a mammal and its species is {var6}.")
    elif menu == 4:
        print("\nYour selection: Bird")
        var6 = input("\nEnter your patient's species: ")
        print(f"\nYour patient called {var3} is a bird and its species is {var6}.")
    elif menu == 5:
        print("\nYour selection: Reptile")
        var6 = input("\nEnter your patient's species: ")
        print(f"\nYour patient called {var3} is a reptile and its species is {var6}.")
    else:
        print("\nAn error has occured! Please, select a kind of patient from the menu.")
        print("You haven't defined your patient's species")
        print("We can't offer an accurate diagnostic without this important information.")
except:
    pass
           
    # We show now the variables where we keep the
    # physiological parameters that will be asked for in consultation

if menu == 1 or menu == 2 or menu == 3 or menu == 4 or menu == 5:
    try:
        sex = input(f"\nEnter {var3}'s sex (M/F): ")
        print(f"\n{var3}'s sex is {sex}.")
   
        age = float(input(f"\nEnter {var3}'s age (years): "))
        if age == 1:
            print(f"\n{var3} is {age} year old.")
        else:
            print(f"\n{var3} is {age} years old.")

        w = float(input(f"\nEnter {var3}'s weight (pounds): "))
        if w == 1:
            print(f"\n{var3} weights {w} pound.")
        else:
            print(f"\n{var3} weights {w} pounds.")

        t = float(input(f"\nEnter {var3}'s temperature (ºF): "))
        print(f"\n{var3}'s temperature is {t} ºF.")
        if menu == 1:
            if t < 99.5:
                print(f"-> Warning: {var3}'s temperature is below normal.")
            elif t > 102.6:
                print(f"-> Warning: {var3}'s temperature is above normal.")
            else:
                print(f"-> {var3}'s temperature is in the normal range.")
        elif menu == 2:
            if t < 100.4:
                print(f"-> Warning: {var3}'s temperature is below normal.")
            elif t > 102.6:
                print(f"-> Warning: {var3}'s temperature is above normal.")
            else:
                print(f"-> {var3}'s temperature is in the normal range.")
        else:
            print("\nWe don't have data for this species currently.")
            print("We recommend a diagnostic from an specialist.")
        
        ppm = int(input(f"\nEnter {var3}'s pulse (ppm): "))
        print(f"\n{var3} has {ppm} pulses per minute.")
        if menu == 1:
            if ppm < 60:
                print(f"-> Warning: {var3}'s pulse is below normal.")
            elif ppm > 180:
                print(f"-> Warning: {var3}'s pulse is above normal.")
            else:
                print(f"-> {var3}'s pulse is in the normal range.")
        elif menu == 2:
            if ppm < 140:
                print(f"-> Warning: {var3}'s pulse is below normal.")
            elif ppm > 220:
                print(f"-> Warning: {var3}'s pulse is above normal.")
            else:
                print(f"-> {var3}'s pulse is in the normal range.")
        else:
            print("\nWe don't have data for this species currently.")
            print("We recommend a diagnostic from an specialist.")

        fc = int(input(f"\nEnter {var3}'s cardia rate (bpm): "))
        print(f"\n{var3}'s cardiac rate is {fc} beats per minute.")
        if menu == 1:
            if fc < 60:
                print(f"-> Warning: {var3}'s cardiac rate is below normal.")
            elif fc > 180:
                print(f"-> Warning: {var3}'s cardiac rate is above normal.")
            else:
                print(f"-> {var3}'s cardiac rate is in the normal range.")
        elif menu == 2:
            if fc < 140:
                print(f"-> Warning: {var3}'s cardiac rate is below normal.")
            elif fc > 220:
                print(f"-> Warning: {var3}'s cardiac rate is above normal.")
            else:
                print(f"-> {var3}'s cardiac rate is in the normal range.")
        else:
            print("\nWe don't have data for this species currently.")
            print("We recommend a diagnostic from an specialist.")

        fr = int(input(f"\nEnter {var3}'s respiratory rate (bpm): "))
        print(f"\n{var3}'s respiratory rate is {fr} breaths per minute.")
        if menu == 1:
            if fr < 10:
                print(f"-> Warning: {var3}'s respiratory rate is below normal.")
            elif fr > 30:
                print(f"-> Warning: {var3}'s respiratory rate is above normal.")
            else:
                print(f"-> {var3}'s respiratory rate is in the normal range.")
        elif menu == 2:
            if fr < 20:
                print(f"-> Warning: {var3}'s respiratory rate is below normal.")
            elif fr > 42:
                print(f"-> Warning: {var3}'s respiratory rate is above normal.")
            else:
                print(f"-> {var3}'s respiratory rate is in the normal range.")
        else:
            print("\nWe don't have data for this species currently.")
            print("We recommend a diagnostic from an specialist.")

        crefill = float(input(f"\nEnter {var3}'s capillary refill (seconds): "))
        if crefill <= 1:
            print(f"\n{var3}'s capillary refill is below 1 second.")
            print(f"-> {var3}'s capillary refill is in the normal range.")
        elif crefill <= 2:
            print(f"\n{var3}'s capillary refill is below 2 seconds.")
            print(f"-> {var3}'s capillary refill is in the normal range.")
        else:
            print(f"\n{var3}'s capillary refill is above 2 seconds.")
            print(f"-> Warning: {var3}'s capillary refill is above normal.")

        print("\nClinical history has been updated succesfully...")
    except:
        pass

    # Once we've met the physiological parameters of our patient, then we proceed
    # to ask for the key information that could give us a better understanding
    # to have a complete diagnostic

print("\n|--------------------------------------|")

var7 = input("\nEnter your consultation reason: ")
var8 = input("\nEnter the evolution of illness: ")
var9 = input("\nApetite: ")
var0 = input("\nBehaviour: ")
print(f"\n{var3}'s key report:")
print(f"Consultation reason: {var7}.")
print(f"Evolution of illness: {var8}.")
print(f"Apetite: {var9}.")
print(f"Behaviour: {var0}.")
print("\nClinical history has been updated succesfully...")

    # Now we make a physical examination to our patient

print("\n|--------------------------------------|")
print(f"\n{var3}'s physical examination:\n")

try:
    print("Body Condition->")
    bc = {1:"1. Very thin", 2:"2. Thin", 3:"3. Ideal weight",
          4:"4. Overweight", 5:"5. Obese"}
    for value in bc:
        print(bc[value])
    bc = int(input(f"\nEnter {var3}'s body condition: "))
    if menu == 1:
        if bc == 1:
            print(f"\n{var3} has a very thin body condition.")
        elif bc == 2:
            print(f"\n{var3} has a thin body condition.")
        elif bc == 3:
            print(f"\n{var3} has an ideal body condition.")
        elif bc == 4:
            print(f"\n{var3} has overweight.")
        elif bc == 5:
            print(f"\n{var3} is highly obese.")
        else:
            print(f"\nAn error has ocurred! Wrong value.")
    elif menu == 2:
        if bc == 1:
            print(f"\n{var3} has a very thin body condition.")
        elif bc == 2:
            print(f"\n{var3} has a thin body condition.")
        elif bc == 3:
            print(f"\n{var3} has an ideal body condition.")
        elif bc == 4:
            print(f"\n{var3} has overweight.")
        elif bc == 5:
            print(f"\n{var3} is highly obese.")
        else:
            print(f"\nAn error has ocurred! Wrong value.")
    else:
        print("\nWe don't have data for this species currently.")
        print("We recommend a diagnostic from an specialist.")
        
    print("\nClinical history has been updated succesfully...")
except:
    pass

print("\nThank you for trusting us...")
