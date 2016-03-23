MENU_STR = "\n(E)ven \n(O)dd \n(S)quares"

lowerbound = int(input("Enter the lower range boundary: "))
upperbound = int(input("Enter the upper range boundary: "))

menuChoice = input(MENU_STR).upper()

while menuChoice != "Q":
    if menuChoice == "E":
        if lowerbound % 2 == 1:
            for i in range(lowerbound +1, upperbound, 2):

                print(i, end=" ")
        else:
            for i in range(lowerbound, upperbound, 2):
                print(i, end=" ")
    elif menuChoice == "O":
        if lowerbound % 2 == 1:
            for i in range(lowerbound, upperbound, 2):
                print(i, end=" ")
        else:
            for i in range(lowerbound + 1, upperbound, 2):
                print(i, end=" ")
    elif menuChoice == "S":
        for i in range(lowerbound, upperbound):
            print(i**2, end=" ")
    else:
        print("Invalid input,\ntry again")
    menuChoice = input(MENU_STR).upper()
print("Goodbye")