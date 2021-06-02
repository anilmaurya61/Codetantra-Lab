s=input("Input comma separated sequence of words: ")
words=[word for word in s.split(",")]
print(",".join(sorted(list(set(words)))))