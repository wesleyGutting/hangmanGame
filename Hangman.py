import os

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def checkGuess(list, guess):
    correctList = []
    flag = 0
    for letter in list:
        if guess == letter:
            correctList.append(1)
            flag = 1
        else:
            correctList.append(0)

    return flag, correctList

def render():
    clearScreen()
    print("Bruh")

clearScreen()
solution = input("Welcome to the hangman game, please enter the word you would like to play for:\n\n").upper()
letters = set(list(solution))

tries = 0
correctGs = 0

while(tries < 6):
    guess = input("Which letter would you like to guess?\n").upper()

    flag, check = checkGuess(letters, guess)

    if flag == 1:
        print("Correct!")
        correctGs += 1
    else:
        print("Incorrect!")
        tries += 1

    if(correctGs == len(letters)):
        winner = True
        break

    print(f"You have {5-tries} tries left")

clearScreen()
if(winner == True):
    print("CONGRATS!!!")
else:
    print("Better Luck Next Time!!!")
