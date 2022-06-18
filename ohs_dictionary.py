print("\t\t\t····················")
print("\t\t\t:··OHS DICTIONARY··:")
print("\t\t\t····················")

print("\nWelcome to the OHS DICTIONARY for students.")
print("\t________________________________________________________________")

var1 = input("\nFirst Name: ")
var2 = input("\nLast Name: ")
var3 = input("\nID: ")

print(f"\nHello, {var1}. Feel free to navigate through the concepts of OHS.")
print("\n:Menu:\n")
var4 = {1:'1-Occupational Safety.', 2:'2-Occupational Health.'}
for value in var4:
    print(var4[value])
var4 = int(input("\nSelect the field you wish to investigate: "))

if var4 == 1: #Occupational Safety
    print("\nModule: Occupational Safety.\n")
    os = {1:'1-Mechanical Hazard.', 2:'2-Electrical Hazard.',
              3:'3-Accident Investigation.', 4:'4-Emergency Brigade.'}
    for value in os:
        print(os[value])
    os = int(input("\nYour choice: "))

    #mechanical hazard
    if os == 1:
        print("\nSelect:\n")
        os1 = {1:'1-Fall on the same level.', 2:'2-Fall from heights.',3:'3-Entanglement.'}
        for value in os1:
            print(os1[value])
        os1 = int(input("\nYour choice: "))

        if os1 == 1:
            print("\nDefinition:\
                        \nA fall on the same level refers to people, in this case: workers,\
                        \nslipping or tripping on the surface they are walking on and fall\
                        \nto the same level of the floor, which results in injury.")
        elif os1 == 2:
            print("\nDefinition:\
                        \nIt refers to falling from one level to another, and it can be as small\
                        \na distance as falling from the first rung of a ladder, or as high as\
                        \nfalling from a high-rise building.")
        elif os1 == 3:
            print("\nDefinition:\
                        \nIt refers to a person becoming pinched, crushed or wrapped in any part\
                        \nof a machine. Machines pose a hazard of entanglement when they have\
                        \nany of the following points:\
                        \n·Two or more parts moving at the same time (pinch point).\
                        \n·Two or more parts moving towards one another (crush point).\
                        \n·Rotating components becoming exposed (wrap point).")
        else:
            print("\nAn error has ocurred.\
                      \nPlease, try again.")

    #electrical hazard
    elif os == 2:
        print("\nSelect:\n")
        os2 = {1:'1-Live circuits.', 2:'2-Improper grounding.',3:'3-Damaged extension cords.'}
        for value in os2:
            print(os2[value])
        os2 = int(input("\nYour choice: "))

        if os2 == 1:
            print("\nDefinition:\
                        \nIt refers to a circuit that has power actively passing through it, in other words,\
                        \nthe power source is turned on. Even if the worker isn't hurt by the shock he can\
                        \nbe startled and jump or fall backwards into another person or an object.\
                        \nThe workers who take shortcuts with live circuits end up hurting themselves\
                        \nor those around them.")
        elif os2 == 2:
            print("\nDefinition:\
                        \nAn improper grounding enables the flow of electricity to run through the human\
                        \nbody making it available to suffer any injury. Examples of this could be a ground\
                        \nwith unattached wires or a broken ground on the end of extention cords.")
        elif os2 == 3:
            print("\nDefinition:\
                        \nThere are many cases where cords have damaged insulations and bare copper wire\
                        \nis showing. It's recommended to throw away any damaged cord and only use new\
                        \nones.")
        else:
            print("\nAn error has ocurred.\
                      \nPlease, try again.")

    #accident investigation
    elif os == 3:
        print("\nSelect:\n")
        os3 = {1:'1-Material causes.', 2:'2-Environmental causes.',3:'3-Personnel causes.'}
        for value in os3:
            print(os3[value])
        os3 = int(input("\nYour choice: "))

        if os3 == 1:
            print("\nDefinition:\
                        \nInvestigators might ask ->\
                        \nWas there an equipment failure?\
                        \nWhat caused it to fail?\
                        \nWere hazardous products involved?")
        elif os3 == 2:
            print("\nDefinition:\
                        \nInvestigators may want to know ->\
                        \nWhat were the weather conditions?\
                        \nWas noise a problem?\
                        \nWas there adequate light?")
        elif os3 == 3:
            print("\nDefinition:\
                        \nInvestigators may want to know ->\
                        \nDid the worker follow the safe operating procedures?\
                        \nWere workers experienced in the work being done?\
                        \nWere they tired?")
        else:
            print("\nAn error has ocurred.\
                      \nPlease, try again.")

    #emergency brigade
    elif os == 4:
        print("\nSelect:\n")
        os4 = {1:'1-Evacuation brigade.', 2:'2-First aid brigade.',3:'3-Fire brigade.'}
        for value in os4:
            print(os4[value])
        os4 = int(input("\nYour choice: "))

        if os4 == 1:
            print("\nDefinition:\
                        \nThis brigade crafts and applies the procedures for the evacuation\
                        \nof the population of the property in an emergency.")
        elif os4 == 2:
            print("\nDefinition:\
                        \nThis brigades carries out the help for those in need, it responds to\
                        \na specific situation that is related with people and care for people while\
                        \nmedical professionals arrive.")
        elif os4 == 3:
            print("\nDefinition:\
                        \nThis brigade will eliminate the risks that may induce fire in different areas.\
                        \nThey take action in two important phases, the PREVENTION PHASE is where\
                        \nthey make inspections to all the equipment (extiguishers, electric installation, etc.)\
                        \nand identify hazards, and the RESPONSE PHASE where they intervene in the\
                        \naffected area.")
        else:
            print("\nAn error has ocurred.\
                      \nPlease, try again.")

    else:
        print("\nAn error has ocurred.\
                  \nPlease, try again.")

elif var4 == 2: #Occupational Health
    print("\nModule: Occupational Health.\n")
    oh = {1:'1-Physical Hazard.', 2:'2-Chemical Hazard.',
               3:'3-Biological Hazard.', 4:'4-Ergonomic and Psychosocial Hazard.'}
    for value in oh:
        print(oh[value])
    oh = int(input("\nYour choice: "))

    #physical hazard
    if oh == 1:
        print("\nSelect:\n")
        oh1 = {1:'1-Temperature.', 2:'2-Radiation.',3:'3-Vibrations.'}
        for value in oh1:
            print(oh1[value])
        oh1 = int(input("\nYour choice: "))

        if oh1 == 1:
            print("\nDefinition:\
                        \nHigh temperatures and humidity stress the body's ability to cool itself,\
                        \nand heat illness becomes a special concern during hot weather. Exposure to\
                        \nfreezing and cold temperatures for extended periods of time may cause\
                        \nserious health problems such as trench foot, frostbite and hypothermia. ")
        elif oh1 == 2:
            print("\nDefinition:\
                        \nExposure to very high levels of radiation, such as being close to an\
                        \natomic blast, can cause acute health effects such as skin burns and\
                        \nacute radiation syndrome.")
        elif oh1 == 3:
            print("\nDefinition:\
                        \nVibration induces health conditions progress slowly. In the beginning it\
                        \nusually starts as a pain. As the vibration exposure continues, the pain may\
                        \ndevelop into an injury or disease.")
        else:
            print("\nAn error has ocurred.\
                      \nPlease, try again.")

    #chemical hazard
    elif oh == 2:
        print("\nSelect:\n")
        oh2 = {1:'1-Corrosives.', 2:'2-Irritants.',3:'3-Carcinogens.'}
        for value in oh2:
            print(oh2[value])
        oh2 = int(input("\nYour choice: "))

        if oh2 == 1:
            print("\nDefinition:\
                        \nCorrosives can be in the liquid, solid, or gaseous state.\
                        \nCorrosive chemicals can have a severe effect on eyes, skin,\
                        \nrespiratory tract, and gastrointestinal tract if an exposure occurs.")
        elif oh2 == 2:
            print("\nDefinition:\
                        \nIrritants are substances that may cause injuries to the skin,\
                        \nthe eyes or airways after a single exposure. These injuries may\
                        \nrange from small, initially invisible injuries after exposure to weak\
                        \nirritants up to chemical burns after exposure to very strong irritants.")
        elif oh2 == 3:
            print("\nDefinition:\
                        \nCarcinogens are agents that can cause cancer. In industry, there are\
                        \nmany potential exposures to carcinogens. Generally, workplace exposures\
                        \nare considered to be at higher levels than for public exposures.")
        else:
            print("\nAn error has ocurred.\
                      \nPlease, try again.")

    #biological hazard
    elif oh == 3:
        print("\nSelect:\n")
        oh3 = {1:'1-Bacteria.', 2:'2-Virus.',3:'3-Fungi.'}
        for value in oh3:
            print(oh3[value])
        oh3 = int(input("\nYour choice: "))

        if oh3 == 1:
            print("\nDefinition:\
                        \nBacteria are microscopic, single-celled organism that exist in every\
                        \nenvironment, both inside and outside other organisms.")
        elif oh3 == 2:
            print("\nDefinition:\
                        \nA virus is an infective agent that typically consists of a nucleic\
                        \nacid molecule in a protein coat, is too small to be seen by light\
                        \nmicroscopy and is able to multiply only within the living cells of\
                        \na host.")
        elif oh3 == 3:
            print("\nDefinition:\
                        \nIt refers to any of a group of spore-producing organisms feeding\
                        \non organic matter, including molds, yeast, mushrooms, and toadstools.")
        else:
            print("\nAn error has ocurred.\
                      \nPlease, try again.")

    #ergonomic and psychosocial hazard
    elif oh == 4:
        print("\nSelect:\n")
        oh4 = {1:'1-Repetition.', 2:'2-Awkward posture.',3:'3-Harassment.'}
        for value in oh4:
            print(oh4[value])
        oh4 = int(input("\nYour choice: "))

        if oh4 == 1:
            print("\nDefinition:\
                        \nIn the context of workplace ergonomics, repetition is defined as\
                        \nthe number of similar exertions performed while engaging in a work-related task.")
        elif oh4 == 2:
            print("\nDefinition:\
                        \nAwkward posture refers to positions of the body that deviate\
                        \nsignificantly from the neutral position while performing work\
                        \nactivities. When you are in an awkward posture, muscles operate\
                        \nless efficiently and you expend more force to complete the task.")
        elif oh4 == 3:
            print("\nDefinition:\
                        \nWorkplace harassment is the belittling or threatening behavior\
                        \ndirected at an individual worker or a group of workers.")
        else:
            print("\nAn error has ocurred.\
                      \nPlease, try again.")

else:
    print("\nAn error has ocurred.\
                \nPlease, try again.")
