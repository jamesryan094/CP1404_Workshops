my_file = open("name.txt", "r")
for line_str in my_file:
    print("your name is", line_str)
my_file.close