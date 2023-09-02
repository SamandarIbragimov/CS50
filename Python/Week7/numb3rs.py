import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        l = [int(matches.group(i)) for i in range(1,5)]
        print(l)
        if any(l[i] not in range(0,256) for i in range(0,4)):
            return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    main()