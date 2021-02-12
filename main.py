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


def computergameloop():
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



# def worstcase_strategy(all_codes, feedback, guess):
#     all_answers = all_codes.copy()
#     for i in all_codes:
#         for j in all_answers







#def 1worstcase_strategy(all_codes, feedback, guess):
    """als je een code raad, hoeveel geven dit antwoord
    bvb AABB geeft max 256
    je loopt eerst door alle vragen heen, (all possible codes)
    voor elke vraag kijk je naar elke mogelijke code sla op hoevaak je elke feedback krijgt
    binnen de vraag onthoudt de worst cases
    binnen een vraag kijk naar het hoogste getal binnen de feedback, dat is de worst worst case, sla alle worst case op, en kies de beste uit de worst case scenarios"""




def codegen():
    """generates a list of possible codes from the existing colors,
    currently only works for a max of 4 different colors"""
    generatedCodes = []
    for index1 in COLORLST:
        for index2 in COLORLST:
            for index3 in COLORLST:
                for index4 in COLORLST:
                    generatedCodes.append([index1,index2, index3, index4])
    return(generatedCodes)



gameloop()
