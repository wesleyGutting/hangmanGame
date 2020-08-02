import os

GUESSED_LIST = []

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def checkGuess(list, guess):
    for letter in list:
        if ((guess == letter) and (guess not in GUESSED_LIST)):
            GUESSED_LIST.append(guess)
            return 1
        elif ((guess == letter) and (guess in GUESSED_LIST)):
            return 2
        else:
            flag = 0
    return flag

def render(wrong, right):
    clearScreen()
    print("------------------------------")
    if(wrong >= 1):
        print("-------------O----------------")
    else:
        print("------------------------------")
    if(wrong == 2):
        print("-------------|----------------")
    elif(wrong == 3):
        print("------------\|----------------")
    elif(wrong >= 4):
        print("------------\|/---------------")
    else:
        print("------------------------------")
    if(wrong == 5):
        print("------------/-----------------")
    elif(wrong == 6):
        print("------------/-\---------------")
    else:
        print("------------------------------")
    print("------------------------------")


clearScreen()
render(6, 0)
solution = input("Welcome to the hangman game, please enter the word you would like to play for:\n").upper()
letters = set(list(solution))

tries = 0
correctGs = 0
winner = False

while(tries < 6):
    #render(tries, correctGs)
    guess = input("Which letter would you like to guess?\n").upper()

    flag = checkGuess(letters, guess)

    if flag == 1:
        print("Correct!")
        correctGs += 1
    elif flag == 2:
        print("You already guessed that")
    elif flag ==0:
        print("Incorrect!")
        tries += 1
        print(f"You have {6-tries} errors left")

    if(correctGs == len(letters)):
        winner = True
        break

clearScreen()
if(winner == True):
    print("CONGRATS!!!")
else:
    print("Better Luck Next Time!!!")
