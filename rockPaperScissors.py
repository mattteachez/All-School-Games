#Game Code

#Import functions
import time
import random
import string
import sys

#Bot game code
def botGame():    
    print("Chose your option: ")

    time.sleep(1)
    print("(1) Rock")
    time.sleep(0.5)
    print("(2) Paper")
    time.sleep(0.5)
    print("(3) Scissors")

    playerChoice = input("\n")
    botChoice = random.randint(1, 3)

    print("So the results are....")

    for i in range(3):
        print(3 - i, end = "")
        time.sleep(0.7)

    print("\n")
        
    if playerChoice == "1" and botChoice == 3:
        print("Player one wins!")

    elif playerChoice == "3" and botChoice == 1:
        print("Bot wins!")

    elif playerChoice == "2" and botChoice == 3:
        print("Bot wins!")

    elif playerChoice == "3" and botChoice == 2:
        print("Player one wins")

    elif playerChoice == "2" and botChoice == 1:
        print("Player one wins")

    elif playerChoice == "1" and botChoice == 2:
        print("Bot wins!")

    elif playerChoice == botChoice or botChoice == playerChoice:
        print("Tie!")


print("This is a simple game of rock, paper, scissors")

print("So, before we start, do you want to play with a friend or with a bot?")
time.sleep(1)
print("(1) Friend")
time.sleep(0.5)
print("(2) Bot")

playerChoice = input("\n")
time.sleep(0.5)

if playerChoice == "1":
    print("\nFirst, player 2, close your eyes as player 1 choses an option.")
    time.sleep(1)
    print("Player one, chose your option: ")

    time.sleep(1)
    print("(1) Rock")
    time.sleep(0.5)
    print("(2) Paper")
    time.sleep(0.5)
    print("(3) Scissors")

    playerOneChoice = input("\n")

    for i in range(100):
        print("\n")

    print("\nOk now player 1 close your eyes as player 2 choses an option")
    time.sleep(1)
    print("Player two, chose your option: ")

    time.sleep(1)
    print("(1) Rock")
    time.sleep(0.5)
    print("(2) Paper")
    time.sleep(0.5)
    print("(3) Scissors")

    playerTwoChoice = input("\n")

    for i in range(100):
        print("\n")


    print("So the results are....")

    for i in range(3,0,-1):
        print(i)
        time.sleep(0.7)

    print("\n")

    if playerOneChoice == "1" and playerTwoChoice == "3":
        print("Player one wins!")

    elif playerOneChoice == "3" and playerTwoChoice == "1":
        print("Player two wins!")

    elif playerOneChoice == "2" and playerTwoChoice == "3":
        print("Player two wins")

    elif playerOneChoice == "3" and playerTwoChoice == "2":
        print("Player one wins")

    elif playerOneChoice == "2" and playerTwoChoice == "1":
        print("Player one wins")

    elif playerOneChoice == "1" and playerTwoChoice == "2":
        print("Player two wins")

    elif playerOneChoice == playerTwoChoice or playerTwoChoice == playerOneChoice:
        print("Tie!")

elif playerChoice == "2":
    botGame()

else:
    print("Due to invalid imput, you will go against a bot!")
    time.sleep(1)
    botGame()

    
    



