import random
import itertools
from constants import AMOUNT_TO_GUESS, AMOUNT_OF_TRIES, COLORLST


"""Mastermind game. constant variables are located in the file "constants.py"""


"""base mastermind functions: masterCode, codegen, blackCheck, whiteCheck"""
def masterCode(COLORLST):
    """generates a code that needs to be guessed using the COLORLST and
    AMOUNT_TO_GUESS variable from the constants file.
    COLORLST are the different colors that can be used to generate a code.
    AMOUNT_TO_GUESS is the amount of colors the user/AI needs to guess."""
    master = []
    for i in range(0, AMOUNT_TO_GUESS):
        r = random.choice(COLORLST)
        master.append(r)
    print(f"master code: {master}")
    return master


def codegen():
    """generates a list of all possible codes based on the colors in COLORLST"""
    generatedCodes = [list(i) for i in list(itertools.product((COLORLST), repeat=AMOUNT_TO_GUESS))]
    return(generatedCodes)


def blackCheck(code, guesslst):
    """checks if there are any guesses in the right place (making them black pins)
     and also calls the check for the white pins"""
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



def gameloop():
    """starts the game and keeps it going until the code is guessed or the tries run out.
    https://www.tutorialspoint.com/python-get-a-list-as-input-from-user this discribes the:
    list(map(str, input("make a guess: ").strip().split(',')))[:AMOUNT_TO_GUESS] part of the code,
    it makes a list out of the users input."""
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


def computergameloop_simple():
    """starts the simple game loop.
    the simple game loop uses the simple_strategy function to guess the master code."""
    all_codes = codegen()
    code = masterCode(COLORLST)
    for i in range(AMOUNT_OF_TRIES):
        guess = random.choice(all_codes)
        feedback = blackCheck(code, guess)
        print(f"guess is : {guess}")
        print(feedback)
        all_codes = simple_strategy(all_codes, feedback, guess)
        print(f"{len(all_codes)}\n")
        if guess == code:
            print("You won!!")
            exit()


def simple_strategy(all_codes, feedback, guess):
    """this loops trough all the codes and creates a new list with the codes that are still possible"""
    possible_codes = []
    for i in all_codes:
        if feedback == blackCheck(guess, i):
            possible_codes.append(i)
    return possible_codes



def computergameloop_worstcase():
    """starts the worstcase gameloop
    the worst case gameloop uses the worstcase_strategy function
    it also uses the simple_strategy function to make the new list of possible codes"""
    all_codes = codegen()
    code = masterCode(COLORLST)
    for i in range(AMOUNT_OF_TRIES):
        guess = worstcase_strategy(all_codes)
        feedback = blackCheck(code, guess)
        print(f"guess is : {guess}")
        print(f"feedback is : {feedback}")
        all_codes = simple_strategy(all_codes, feedback, guess)
        print(f" len all codes: {len(all_codes)}\n")
        if guess == code:
            print("You won!!")
            exit()


def worstcase_strategy(all_codes):
    """the worst case strategy finds out what the move is that gives the best worstcase scenario,
    it also refrences the old moves the player/AI has made to choose the best next move"""
    possibilities = all_codes.copy()
    feedbackdict = {}
    worstcasedict = {}
    for i in possibilities:
        for j in possibilities:
            feedback = blackCheck(i, j)
            if feedback in feedbackdict:
                feedbackdict[feedback] += 1
            else:
                feedbackdict[feedback] = 1
        worstcase = max(feedbackdict.values())
        worstcasedict[tuple(i)] = worstcase
        feedbackdict = {}
    bestworstcase = min(worstcasedict, key=worstcasedict.get)
    return list(bestworstcase)



def computergameloop_own():
    """a fairly simple strategy that just chooses the first item in the list of possible answers.
    this works in a very similar way to the simple_strategy"""
    all_codes = codegen()
    code = masterCode(COLORLST)
    for i in range(AMOUNT_OF_TRIES):
        guess = all_codes[0]
        feedback = blackCheck(code, guess)
        print(f"guess is : {guess}")
        print(feedback)
        all_codes = simple_strategy(all_codes, feedback, guess)
        print(f"{len(all_codes)}\n")
        if guess == code:
            print("You won!!")
            exit()


computergameloop_worstcase()
