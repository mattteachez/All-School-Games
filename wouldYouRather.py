
#Game Code

#Import functions
import time
import random
import string
import sys

WYROne = [
"lose the ability to read", "be covered in fur",
"be in jail for a year", "always be 10 minutes late",
"a key that opens any door", "know the history of every object you touched",
"be able to talk to land animals, animals that fly,",
"have all traffic lights you approach be green",
"be the first person to explore a planet"
]

WYRTwo = [
"lose the ability to speak", "be covered in scales",
"lose a year of you life", "always be 20 minutes early",
"have one real get out of jail free card", "be able to talk to animals",
"animals that live under the water", "never have to stand in line again",
"be the inventor of a drug that cures a deadly disease"
]



print("This is would you rather!")

time.sleep(1)

print("You will get two choices, and will have to choose between them!")

time.sleep(2)

print("Do you want random or matched?")

time.sleep(1)

print("\n1) Random")
time.sleep(.10)
print("2) Matched")
time.sleep(.10)

choice = input("\n")

if choice == "1":
    print("Ok, you have chosen random!")
    
    def choiceOne():
        time.sleep(1)
        oneW = random.choice(WYROne)
        twoW = random.choice(WYRTwo)
        
        print("Would You rather " + oneW + " or " + twoW + "?")

        randomm = input("")

        if randomm == "exit":
            sys.exit

        else:
            choiceOne()

    choiceOne()

elif choice == "2":
    print("You have chosen matched!")
    
    def choiceTwo():

        time.sleep(1)

        WYR = ["1", "2", "3", "4", "5", "5", "6", "7", "8", "9", "10" , "11", "12", "13",
           "14", "15"]

        WYRMatchChoice = random.choice(WYR)


        if WYRMatchChoice == "1":
            print("Would you rather the aliens that make first contact be robotic or organic?")

        elif WYRMatchChoice == "2":
            print("Would you rather lose the ability to read or lose the ability to speak?")

        elif WYRMatchChoice == "3":
            print("Would you rather be covered in fur or covered in scales?")

        elif WYRMatchChoice == "4":
            print("Would you rather be in jail for a year or lose a year off your life?")

        elif WYRMatchChoice == "5":
            print("Would you rather always be 10 minutes late or always be 20 minutes early?")

        elif WYRMatchChoice == "6":
            print("Would you rather have one real get out of jail free card or a key that opens any door?")

        elif WYRMatchChoice == "7":
            print("Would you rather know the history of every object you touched or be able to talk to animals?")

        elif WYRMatchChoice == "8":
            print("Would you rather be able to talk to land animals, animals that fly, or animals that live under the water?")

        elif WYRMatchChoice == "9":
            print("Would you rather have all traffic lights you approach be green or never have to stand in line again?")

        elif WYRMatchChoice == "10":
            print("Would you rather spend the rest of your life with a sailboat as your home or an RV as your home?")

        elif WYRMatchChoice == "11":
            print(" Would you rather give up all drinks except for water or give up eating anything that was cooked in an oven?")

        elif WYRMatchChoice == "12":
            print("Would you rather be able to see 10 minutes into your own future or 10 minutes into the future of anyone but yourself?")

        elif WYRMatchChoice == "13":
            print("Would you rather have an easy job working for someone else or work for yourself but work incredibly hard?")

        elif WYRMatchChoice == "14":
            print("Would you rather be the first person to explore a planet or be the inventor of a drug that cures a deadly disease?")

        elif WYRMatchChoice == "15":
            print("Would you rather go back to age 5 with everything you know now or know now everything your future self will learn?")

        restart = input("")

        if random == "exit":
            sys.exit

        else:
            choiceTwo()

    choiceTwo()
    


