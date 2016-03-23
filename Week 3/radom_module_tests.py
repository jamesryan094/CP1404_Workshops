import random
# num = int(input("enter you num, mang"))
# print(num)
#
# potential_letters = "!@"
#
string_to_generate_password = ""
count = 0
potential_letters = "!@"
word_length = int(input("gimme a no."))

while count < word_length:
    string_to_generate_password += (potential_letters[random.randint(0, (len(potential_letters) - 1))])
    count += 1

print (string_to_generate_password)