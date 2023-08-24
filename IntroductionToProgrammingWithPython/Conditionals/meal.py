def main():
    time = input("What time is it? ").strip()
    n = convert(time)
    if 7 <= n <=8:
       print("breakfast time")
    elif 12 <= n <= 13:
       print("lunch time")
    elif 18 <= n <= 19:
       print("dinner time")


def convert(time):
    h,m = time.split(":")
    h = float(h)
    m = float(m)
    return (h + m/60)


if __name__ == "__main__":
    main()