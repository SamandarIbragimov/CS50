import sys, os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        file1 = os.path.splitext(sys.argv[1])
        file2 = os.path.splitext(sys.argv[2])
        if not file1[1] in [".jpg",".jpeg",".png"]:
            sys.exit("Invalid Input")
        elif not file2[1] in [".jpg",".jpeg",".png"]:
            sys.exit("Invalid Output")
        elif not file1[1] == file2[1]:
            sys.exit("Input and output have different extensions")
        else:
            change(sys.argv[1], sys.argv[2])


def change(file1,file2):
    try:
        shirt = Image.open("shirt.png")
        before = Image.open(file1)
        after = ImageOps.fit(before, shirt.size)
        after.paste(shirt, shirt)
        after.save(file2)

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()