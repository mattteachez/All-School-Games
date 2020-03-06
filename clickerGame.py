import time
import random
import string
import sys

def clickRepeat(clickCount, costs, cl):
    clicks = input("")

    if clicks == "":
        clickCount += cl
        print("{} ".format(clickCount), end = '')
        clickRepeat(clickCount, costs, cl)

    elif clicks == "shop":
        print("Do you want to buy double clicks for {} clicks?".format(costs))
        buy = input("")
        
        if buy == "yes":
            if clickCount > 49:
                print("Thanks for you business")
                clickCount -= costs
                costs *= 10
                cl *= 2
                clickRepeat(clickCount, costs, cl)

            else:
                print("You dont have enough")
                clickRepeat(clickCount, costs, cl)

        else:
            print("Okay")
            clickRepeat(clickCount, costs, cl)

    else:
       clickRepeat(clickCount, costs, cl) 
            

clickRepeat(0, 10, 1)
    
