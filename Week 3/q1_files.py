FILENAME = "name.txt"
name = input("name pls")

name_file = open(FILENAME, "w")
print(name, file=name_file)
name_file.close