sentence = "hash maps are useful and hash maps are fast"
words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequencies:")
for word in word_count:
    print(word, "->", word_count[word])
