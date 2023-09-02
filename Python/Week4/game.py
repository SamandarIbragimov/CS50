from random import randint
import sys

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue
    if level <= 0:
        continue
    else:
        num = randint(1,level)
        while True:
            try:
                guess = int(input("Guess: "))
            except ValueError:
                continue
            if guess < num:
                print("Too small!")
                continue
            elif guess > num:
                print("Too large!")
                continue
            else:
                sys.exit("Just right!")
