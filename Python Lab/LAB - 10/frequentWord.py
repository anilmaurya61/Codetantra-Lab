fname = input("Enter file name: ")
file = open(fname, "r")
frequency_word = ""
frequency = 0
words = []

for line in file:

    line_word = line.lower().replace(',', '').replace('.', '').split(" ")

    for w in line_word:
        words.append(w)

for i in range(0, len(words)):

    count = 1

    for j in range(i+1, len(words)):
        if(words[i] == words[j]):
            count = count + 1

    if(count > frequency):
        frequency = count
        frequency_word = words[i]

print("Most repeated word: " + frequency_word)
print("Frequency: " + str(frequency))
file.close()
