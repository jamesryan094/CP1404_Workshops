number = 0

numbers_file = open("numbers.txt", "r")

for line in numbers_file:
    number += int(line)
print(number)