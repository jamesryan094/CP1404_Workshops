try:
 numerator = int(input("Enter the numerator: "))
 denominator = int(input("Enter the denominator: "))
 fraction = numerator / denominator


except ValueError:
 print("Numerator and denominator must be valid numbers!")


except ZeroDivisionError:
 print("Cannot divide by zero!")

print("Finished.")
#1. when the user input can not be converted to an int, say if alphabetical input was given or no inpout at all
#2. when zero is entered as the denominator
#3. see below:

# try:
#  numerator = int(input("Enter the numerator: "))
#
#
#  denominator = int(input("Enter the denominator: "))
#    while denominator <=0
#        denominator = int(input("Enter the denominator: "))
#
#
#  fraction = numerator / denominator
#
#
# except ValueError:
#  print("Numerator and denominator must be valid numbers!")
#
#
#
# print("Finished.")