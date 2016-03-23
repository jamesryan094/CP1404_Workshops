#priming Reed
sales = float(input("Enter Sales: $"))

#Loop Entry Condition
while sales > 0:
    if sales <1000:
        bonus = sales * 0.1
    else:
        bonus = sales *0.15
    print("bonus is: $", bonus, sep="")
#Priming reed repeated, updates the variable until sentinal value reached
    sales = float(input("Enter Sales: $"))

print("Goodbye")