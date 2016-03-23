#Constants
MENU_STR = "(H)ello \n(G)oodbye \n(Q)uit"

name = input("Enter Name: ")
menuChoice = input(MENU_STR).upper()
while menuChoice != "Q":
    if menuChoice == "H":
        print("Hello,", name)
    elif menuChoice == "G":
        print("Goodbye,", name)
    else:
        print("Invalid input,\ntry again")
    menuChoice = input(MENU_STR).upper()
print("Goodbye")