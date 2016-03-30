numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)
# print(numbers)
first = numbers[0]
last = numbers[-1]
smallest = min(numbers)
largest = max(numbers)
average = sum(numbers)/len(numbers)

print("The first number is", first)
print("The last number is", last)
print("The smallest number is", smallest)
print("The largest number is", largest)
print("The average or the numbers is", average)
