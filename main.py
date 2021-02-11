import random
from constants import AMOUNT_TO_GUESS, AMOUNT_OF_TRIES, COLORLST
"""Master mind game. constant variables are located in the file "constants.py" 
the function "Gameloop" starts the game """


def masterCode(COLORLST):
    """generates the code that the user needs to guess"""
    master = []
    for i in range(0, AMOUNT_TO_GUESS):
        r = random.choice(COLORLST)
        master.append(r)
    print(master)
    return master


def blackCheck(code, guesslst):
    """checks if there are any guesses in the right place (making them black pins)
     and also calls the check for the white pins"""
    print(code)
    print(guesslst)
    mastercopy = code.copy()
    black_dots = 0
    for i in range(0, len(guesslst)):
        if guesslst[i] == mastercopy[i]:
            black_dots += 1
    white = whiteCheck(mastercopy, guesslst)
    white_dots = white - black_dots
    return black_dots, white_dots


def whiteCheck(mastercopy, guesslst):
    """the check for the white pins, checks if there are pins in the code that are not in the right spot,
     and returns the amount of the incorrect pins"""
    white_dots = 0
    for i in range(0, len(guesslst)):
        if guesslst[i] in mastercopy:
            mastercopy.remove(guesslst[i])
            white_dots += 1
    return white_dots



def gameLoop():
    """starts the game and keeps it going until the code is guessed or the tries run out.
    https://www.tutorialspoint.com/python-get-a-list-as-input-from-user this discribes the:
    list(map(str, input("make a guess: ").strip().split(',')))[:AMOUNT_TO_GUESS] function.
    """
    code = masterCode(COLORLST)
    tries = 0
    stop = False
    while tries < AMOUNT_OF_TRIES or stop == True:
        guesslst = list(map(str, input("make a guess: ").upper().strip().split(',')))[:AMOUNT_TO_GUESS]
        print(guesslst)
        black, white = blackCheck(code, guesslst)
        if black == 4:
            return print("you won the game!!")
        else:
            tries += 1
            print(f"amount of black dots: {black}")
            print(f"amount of white dots: {white}")
            print(f"you have {AMOUNT_OF_TRIES - tries} tries left \n")

def computer():
    code = masterCode(COLORLST)
    tries = 0
    stop = False
    black, white = blackCheck(code, ['R', 'R', 'B', 'C'])
    while tries < AMOUNT_OF_TRIES or stop == True:




        if black == 4:
            return print("you won the game!!")
        else:
            tries += 1
            print(f"amount of black dots: {black}")
            print(f"amount of white dots: {white}")
            print(f"you have {AMOUNT_OF_TRIES - tries} tries left \n")


#print(computer())

def toString(List):
    return ''.join(List)




def codes(string, data, last, index):
    lenght = len(string)
    for i in range(lenght):
        data[index] = string[i]
        if index == last:
            print(toString(data))
        else:
            codes(string, data, last, index+1)

def codes1(string):
    lenght = len(string)
    data = [""] * (lenght+1)
    string = sorted(string)
    codes(string, data, lenght-1, 0)


print(codes1(toString(COLORLST)))

