original_txt = input("Enter a sentence to be counted: ")
unique_words = {}
user_txt = original_txt.lower()
user_txt = user_txt.split()
for word in user_txt:
    if word not in unique_words:
        unique_words[word] = 1
    else:
        unique_words[word] += 1

print("Text: ", original_txt)
for word, frequency in sorted(unique_words.items()):
    print(word,":", frequency)