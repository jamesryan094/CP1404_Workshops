#Special char string taked from worksheet
SPECIAL_CHAR = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"

#set the while loop sentinal value to cause the program to enter the loop
is_valid = False

password = input("Enter Password:")

while not is_valid:
#initialise the counts
    count_upper = 0
    count_lower = 0
    count_numeric = 0
    count_special = 0

    if len(password) < 5 or len(password) > 15:
        print("Invalid password, please try again")
        password = input("Enter Password:")

    for char in password:
        if char == char.upper():
            count_upper += 1

        if char == char.lower():
            count_lower += 1

        if char.isnumeric():
            count_numeric += 1

        if char in SPECIAL_CHAR:
            count_special += 1

    if count_upper > 0 and count_lower > 0 and count_numeric > 0 and count_special > 0:
        is_valid = True
    else:
        print("Invalid password, please try again")
        password = input("Enter Password:")

print(password)