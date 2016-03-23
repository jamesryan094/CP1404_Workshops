finished = False
result = 0
while not finished:
    try:
        result = int(input("enter int"))
        finished = True
    except ValueError:
        print("Please enter a valid integer")
print("valid result is", result)

# int(input("enter int"))  