word = input("camelCase: ")

for c in range(len(word)):
    if word[c].isupper():
        word = word.replace(word[c],"_"+word[c].lower())

print("snake_case: "+word)