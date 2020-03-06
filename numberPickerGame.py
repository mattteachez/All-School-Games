import time
import random
import string
import sys
import shelve

number = int
attempts = int
win = bool
def againPlay():
    print("Pick a number from 1 - 100")
    number = random.randint(0, 100)
    win = False
    attempts = 0
    

    while win == False:
        userInput = input()
        attempts += 1

        if userInput > 100:
            print("Only up to 100, this will not count as an attempt")
            attempts -= 1

        elif userInput > number:
            print("Your number is too big!")
            
        elif userInput < number:
            print("Your number is too small!")

        elif userInput == number:
            print("You win!")

            win = True
            
            time.sleep(3)
            
            print("It took you attempts".format(attempts))
                
            time.sleep(3)
            print("Do you want to play again?")

            again = input("\n")

            again = string.capwords(again)

            if again == "Yes" or again == "Y":
                againPlay()
                print("\n")

            elif again == "No" or again == "N":
                print("Ok, thanks for playing!")
                time.sleep(3)
                sys.exit

            else:
                print("Value invalid. Thanks for playing")
                time.sleep(3)
                sys.exit
                
        else:
            print("Value is invalid #f2%f Error Code 15 #f2%f")

againPlay()



