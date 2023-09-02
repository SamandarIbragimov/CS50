import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a Python file")
        else:
            print(count(sys.argv[1]))


def count(file_name):
    count = 0
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.lstrip().startswith("#") == True or line.isspace() == True:
                    continue
                else:
                    count+=1
    except FileNotFounError:
        sys.exit("File does not exist")

    return count



if __name__ == "__main__":
    main()