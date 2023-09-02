import sys,csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv" or sys.argv[2][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            change(sys.argv[1], sys.argv[2])


def change(file1,file2):
    hogwarts = []
    try:
        with open(file1) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last,first = row["name"].split(", ")
                hogwarts.append({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit("File does not exist")

    with open(file2, "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["first","last","house"])
        writer.writeheader()
        for row in hogwarts:
            writer.writerow({"first": row["first"],"last": row["last"],"house": row["house"]})

if __name__ == "__main__":
    main()