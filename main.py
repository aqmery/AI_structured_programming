import random
import itertools
from constants import AMOUNT_TO_GUESS, AMOUNT_OF_TRIES, COLORLST, AMOUNT_COLORS


"""Master mind game. constant variables are located in the file "constants.py" 
the function "Gameloop" starts the game """


def masterCode(COLORLST):
    """generates the code that the user needs to guess"""
    master = []
    for i in range(0, AMOUNT_TO_GUESS):
        r = random.choice(COLORLST)
        master.append(r)
    print(f"master code: {master}")
    return master


def blackCheck(code, guesslst):
    """checks if there are any guesses in the right place (making them black pins)
     and also calls the check for the white pins"""
    #print(f"master code : {code}")
    #print(f"the guess for the master code: {guesslst}")
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


def computergameloop_simple():
    all_codes = codegen()
    code = masterCode(COLORLST)
    for i in range(AMOUNT_OF_TRIES):
        guess = random.choice(all_codes)
        feedback = blackCheck(code, guess)
        print(f"guess is : {guess}")
        print(feedback)
        all_codes = simple_strategy(all_codes, feedback, guess)
        print(len(all_codes))
        if guess == code:
            print("You won!!")
            exit()


def simple_strategy(all_codes, feedback, guess):
    possible_codes = []
    for i in all_codes:
        if feedback == blackCheck(guess, i):
            possible_codes.append(i)
    return possible_codes


def computergameloop_worstcase():
    all_codes = codegen()
    code = masterCode(COLORLST)
    for i in range(AMOUNT_OF_TRIES):
        guess = worstcase_strategy(all_codes)
        feedback = blackCheck(code, guess)
        print(f"guess is : {guess}")
        print(f"feedback is : {feedback}")
        print(f" len all codes: {len(all_codes)}")
        all_codes = simple_strategy(all_codes, feedback, guess)
        if guess == code:
            print("You won!!")
            exit()


def worstcase_strategy(all_codes):
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
    all_codes = codegen()
    code = masterCode(COLORLST)
    for i in range(AMOUNT_OF_TRIES):
        guess = random.choice(all_codes)
        feedback = blackCheck(code, guess)
        print(f"guess is : {guess}")
        print(feedback)
        all_codes = own_strategy(all_codes, feedback, guess)
        print(len(all_codes))
        if guess == code:
            print("You won!!")
            exit()

def own_strategy(all_codes, feedback, guess):
    possible_codes = []

    return possible_codes











def codegen():
    """generates a list of possible codes from the existing colors"""
    generatedCodes = [list(i) for i in list(itertools.product((COLORLST), repeat=AMOUNT_TO_GUESS))]
    return(generatedCodes)


computergameloop_worstcase()
