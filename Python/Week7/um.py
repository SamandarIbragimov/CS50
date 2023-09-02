import re


def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall("(^|\W)um($|\W)", s, re.IGNORECASE)
    if match:
        return len(match)


if __name__ == "__main__":
    main()