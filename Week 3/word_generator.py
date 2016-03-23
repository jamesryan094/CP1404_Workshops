import random

###
string_to_generate_password = ""
count = 0
potential_letters = "!@"
word_length = int(input("gimme a no."))

while count < word_length:
    string_to_generate_password += (potential_letters[random.randint(0, (len(potential_letters) - 1))])
    count += 1
#print (string_to_generate_password)
###


VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = string_to_generate_password
word = ""

for kind in word_format:
    if kind == "!":
        word += random.choice(CONSONANTS)
    elif kind == "@":
        word += random.choice(VOWELS)
    else:
        word += kind
print(word)
# wd = ""
