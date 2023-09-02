def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not len(s) in [2,3,4,5,6]:
        return False
    if not(s[0].isalpha() and s[1].isalpha()):
        return False
    for c in range(len(s)):
        if s[c].isalpha() == False and s[c].isnumeric() == False:
            return False
    for c in range(len(s)-1):
        if s[c].isalpha() and s[c+1] == "0":
            return False
    for c in range(len(s)-1):
        if s[c].isnumeric() and s[c+1].isalpha():
            return False


    return True


if __name__ == "__main__":
    main()
