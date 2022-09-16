check = input("Are you a student of PCPS ? Type(Yes / No)\n").lower()

if check=="yes" :
    check = input("Which faculty are you belongs to ?\n").upper()
    if check == "BSC" :
        lvl = input("Which level are you from ?\n")
        print("You are study in level : "+lvl+" in "+check+" .")
    else :
        lvl = input("Which level are you from ?\n")
        print("You are study in level : " + lvl + " in " + check + " .")
else :
    print("You are not student of PCPS.")
