def get_number(lower, upper):
    if lower >= upper:
        return lower
    is_valid = False
    while not is_valid:
        try:
            num = int(input("Please enter a number between {} - {} (inclusive):".format(lower, upper)))
            if num in range(lower, upper+1):
                is_valid = True
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("enter a numeral")
    return num


minimum = 33
maximum = 127
print(chr(get_number(minimum, maximum)))




# for i in range(1, 129):
#      print("Character: {}    code: {:>3}".format(chr(i), i))
#      i += 1