#Stats are a very important part of baseball,
#So let's do some stats
print("|::-SHOW YOUR BASEBALL STATS-::|")

player = input("\nEnter player's name: ")
team = input("\nEnter player's team: ")
position = input("\nEnter player's position: ")

print("\n|::-Stats menu-::|\n")
stat = {1:'1.Batting.', 2:'2.Pitching.', 3:'3.Fielding.'}
for value in stat:
    print(stat[value])
stat = int(input("\nChoose a stat to calculate: "))

if stat == 1:
    print("\n|::-Batting stats-::|\n")
    batting = {1:'1.AVG.', 2:'2.SLG.', 3:'3.OBP.', 4:'4.Exit.'}
    for value in batting:
        print(batting[value])
    batting = int(input("\nChoose a batting stat: "))
    # Calculate batting stats
    if batting == 1:
        print("\nBatting average (AVG)->")
        AB = int(input("\nEnter the total 'AT-BATS': "))
        H = int(input("\nEnter the total 'HITS': "))
        AVG = H/AB # Batting average
        print(f"\nThe batting average of {player} is: {AVG:.3f}")
    elif batting == 2:
        print("\nSlugging average (SLG)->")
        AB = int(input("\nEnter the total 'AT-BATS': "))
        H1 = int(input("\nEnter the total 'SINGLE HITS': "))
        H2 = int(input("\nEnter the total 'TWO-BASE HITS': "))
        H3 = int(input("\nEnter the total 'THREE-BASE HITS': "))
        HR = int(input("\nEnter the total 'HOMERUNS': "))
        SLG = (H1+(H2*2)+(H3*3)+(HR*4))/AB # Slugging average
        print(f"\nThe slugging average of {player} is: {SLG:.3f}")
    elif batting == 3:
        print("\nOn-base percentage (OBP)->")
        AB = int(input("\nEnter the total 'AT-BATS': "))
        H = int(input("\nEnter the total 'HITS': "))
        WLK = int(input("\nEnter the total 'WALKS': "))
        HBP = int(input("\nEnter the total 'HIT-BY-PITCH': "))
        SAC_FLY = int(input("\nEnter the total 'SACRIFICE FLIES': "))
        OBP = (H+WLK+HBP)/(AB+WLK+HBP+SAC_FLY) # On-base percentage
        print(f"\nThe on-base percentage of {player} is: {OBP:.3f}")
    elif batting == 4:
        ext = int(input("\nAre you sure you want to exit?\n[Press 0 to exit] -> "))
        if ext == 0:
            print("\nSee you soon with better batting stats...")
        else:
            print("\nRestart the system...")
    else:
        print("\nAn error has ocurred.")
        print("\nWe can't recognize this action.")
elif stat == 2:
    print("\n|::-Pitching stats-::|\n")
    pitching = {1:'1.ERA.', 2:'2.WHIP.', 3:'3.WP.', 4:'4.Exit.'}
    for value in pitching:
        print(pitching[value])
    pitching = int(input("\nChoose a pitching stat: "))
    # Calculate pitching stats
    if pitching == 1:
        print("\nEarned run average (ERA)->")
        IP = float(input("\nEnter the total 'INNINGS PITCHED': "))
        RA = int(input("\nEnter the total 'RUNS ALLOWED': "))
        ERA = (RA*9)/(IP) # Earned run average
        print(f"\nThe earned run average of {player} is: {ERA:.2f}")
    elif pitching == 2:
        print("\nWalks and hits per inning pitched (WHIP)->")
        IP = float(input("\nEnter the total 'INNINGS PITCHED': "))
        H = int(input("\nEnter the total 'HITS ALLOWED': "))
        WLK = int(input("\nEnter the total 'WALKS': "))
        WHIP = (H+WLK)/(IP) # Walks and hits per inning pitched
        print(f"\nThe walks and hits per inning pitched of {player} is: {WHIP:.2f}")
    elif pitching == 3:
        print("\nWinning percentage (WP)->")
        W = int(input("\nEnter the total 'WINNING GAMES': "))
        D = int(input("\nEnter the total 'DECIDED GAMES': "))
        WP = W/D # Winning percentage
        print(f"\nThe winning percentage of {player} is: {WP:.2f}")
    elif pitching == 4:
        ext = int(input("\nAre you sure you want to exit?\n[Press 0 to exit] -> "))
        if ext == 0:
            print("\nSee you soon with better pitching stats...")
        else:
            print("\nRestart the system...")
    else:
        print("\nAn error has ocurred.")
        print("\nWe can't recognize this action.")
elif stat == 3:
    print("\n|::-Fielding stats-::|\n")
    fielding = {1:'FA.', 2:'2.Exit.'}
    for value in fielding:
        print(fielding[value])
    fielding = int(input("\nChoose a fielding stat: "))
    # Calculate the fielding stats
    if fielding == 1:
        print("\nFielding average (FA)->")
        OUT = int(input("\nEnter the total 'PUTOUTS': "))
        A = int(input("\nEnter the total 'ASSITS': "))
        E = int(input("\nEnter the total 'ERRORS': "))
        FA = (OUT+A)/(OUT+A+E) # Fielding average
        print(f"\nThe fielding average of {player} is: {FA:.3f}")
    elif fielding == 2:
        ext = int(input("\nAre you sure you want to exit?\n[Press 0 to exit] -> "))
        if ext == 0:
            print("\nSee you soon with better fielding stats...")
        else:
            print("\nRestart the system...")
    else:
        print("\nAn error has ocurred.")
        print("\nWe can't recognize this action.")
else:
    print("\nAn error has ocurred.")
    print("\nThere are not stats to calculate.")
