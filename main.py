import random
from constants import AMOUNT_TO_GUESS, AMOUNT_OF_TRIES, COLORLST


def mastercode(COLORLST):
    """generates the code that the user needs to guess"""
    master = []
    for i in range(0, AMOUNT_TO_GUESS):
        r = random.choice(COLORLST)
        master.append(r)
    print(master)
    return master


def blackcheck(code, guesslst):
    """checks if there are any guesses in the right place (making them black pins)
     and also calls the check for the white pins"""
    mastercopy = code.copy()
    black_dots = 0
    for i in range(0, len(guesslst)):
        if guesslst[i] == mastercopy[i]:
            black_dots += 1
    whitecheck(mastercopy, guesslst, black_dots)

def whitecheck(mastercopy, guesslst, black_dots):
    """the check for the white pins, checks if there are pins in the code that are not in the right spot,
     and returns the amount of the incorrect pins"""
    white_dots = 0
    for i in range(0, len(guesslst)):
        if guesslst[i] in mastercopy:
            mastercopy.remove(guesslst[i])
            white_dots += 1
    return print(f"amount of white dots: {white_dots - black_dots}")


def GameLoop():
    """starts the game and keeps it going until the code is guessed or the tries run out"""
    code = mastercode(COLORLST)
    tries = 0
    while tries < AMOUNT_OF_TRIES:
        guesslst = list(map(str, input("make a guess: ").strip().split(',')))[:AMOUNT_TO_GUESS]
        tries += 1
        black = blackcheck(code,guesslst)
        if black == 4:
            return "you won the game!!"''
        else:
            f"amount of black dots: {black}"
            print(f"you have {AMOUNT_OF_TRIES - tries} tries left \n")



GameLoop()
