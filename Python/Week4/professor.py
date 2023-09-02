from random import randint


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        first = generate_integer(level)
        second = generate_integer(level)
        flag = False
        for _ in range(3):
            print(first,"+",second,"= ",end="")
            try:
                answer = int(input())
            except ValueError:
                print("EEE")
                continue
            if answer == first + second:
                score +=1
                flag = True
                break
            else:
                print("EEE")
        if flag == False:
            print(first,"+",second,"=",first+second)
        else:
            flag = False
    print("Score:",score)




def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level in [1,2,3]:
            return level


def generate_integer(level):
    if level == 1:
        return randint(0,9)
    elif level == 2:
        return randint(10,99)
    else:
        return randint(100,999)



if __name__ == "__main__":
    main()