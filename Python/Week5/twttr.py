def main():
    print(shorten(input("Input: ")))


def shorten(word):
    for c in word:
        if c in ['a','e','i','o','u','A','E','I','O','U':
            word = word.replace(c, '')
    return word


if __name__ == "__main__":
    main()