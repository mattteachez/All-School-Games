import time
import sys

print("Do you want Ice Cream?")

iceCream = input("")

this_string = "{}Then come and get it".format("\n")
for character_index in this_string:
   print(character_index, end = ' ')
   time.sleep(0.1)

this_stringTwo = "\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░░      ░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░░░░▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░░░░░░░░░  ░░░░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    ░░  ░░░░░░░░░░  ░░░░░░░░░░░░\n░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░  ░░░░    ░░░░░░░░░░░░\n░░░░░░░░▒▒▒▒░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░    ░░░░      ░░  ░░░░░░\n░░░░▒▒░░▒▒▒▒░░░░▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░              ░░  ░░░░\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒░░░░░░▒▒░░░░▒▒▒▒░░░░░░░░▒▒░░░░░░░░░░░░▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░    ░░░░░░    ░░\n▒▒▒▒░░▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░▒▒░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░        ░░░░░░\n▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒░░░░▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░  ░░  ░░\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░  ░░\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░▒▒░░░░░░░░░░  ░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░  \n▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒░░░░  \n▒▒▒▒▒▒▒▒░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒░░▒▒▓▓▒▒░░▒▒▒▒░░░░░░░░  ░░░░░░░░  ░░░░░░░░░░░░▒▒▒▒░░░░░░\n▒▒▒▒▒▒░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓██▓▓▓▓▓▓██▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░\n▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▓▓▒▒▒▒▓▓██████▓▓▓▓▓▓████▓▓██████▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░\n▒▒▒▒▒▒▓▓▓▓▒▒▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓██▓▓▓▓████████▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓████▓▓▓▓████▓▓▓▓▒▒▒▒▓▓▒▒░░░░░░░░░░▒▒░░░░▒▒░░░░░░░░\n▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒░░▒▒▒▒░░▒▒░░░░░░\n▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░\n▒▒▒▒▓▓▓▓▒▒▓▓▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▒▒▒▒▒▒▒▒░░░░\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░▒▒\n▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░▒▒░░\n▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██████▓▓▓▓▓▓▒▒░░░░▒▒▓▓▒▒░░▒▒▒▒░░▒▒▓▓▓▓▓▓██████████▓▓▓▓▓▓▓▓░░▒▒▒▒▒▒▒▒▒▒▓▓██▓▓▒▒░░░░░░▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒\n▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░▒▒▓▓▒▒▒▒▒▒▒▒░░▒▒▒▒▓▓██████████████▓▓▓▓▒▒░░▒▒░░░░▒▒▒▒▓▓▓▓▓▓▒▒░░    ░░░░▒▒▓▓▓▓▓▓▓▓████▓▓▒▒\n▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒░░░░░░░░░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓██████████████▓▓▓▓▒▒░░▒▒▒▒▒▒▒▒░░▓▓▓▓▓▓░░░░          ▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓\n▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▒▒▓▓▒▒░░░░░░░░░░░░░░▒▒▓▓▒▒▒▒▒▒▒▒░░▒▒▓▓▓▓██████████████▓▓▒▒▒▒░░░░░░▒▒▒▒░░░░▒▒▒▒░░              ░░▒▒▓▓▓▓▓▓▓▓▓▓\n▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒▓▓▒▒░░░░▒▒▒▒▒▒▒▒▒▒▓▓██████████▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▒▒▒░░              ░░░░▒▒▓▓▓▓▓▓▓▓\n▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒▓▓▒▒░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒                  ░░▒▒▒▒▓▓▓▓▓▓\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▓▓▓▓▒▒░░░░░░░░░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒░░                  ░░░░▒▒▓▓▓▓▓▓\n░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▓▓▓▓▒▒▒▒▒▒░░▒▒░░▒▒░░▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▒▒░░              ░░░░░░▒▒▒▒▒▒▒▒▒▒\n░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▓▓▓▓▓▓▒▒▒▒▒▒░░▒▒░░░░▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░          ░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓\n░░░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▒▒▓▓▒▒\n▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓▒▒░░▒▒\n░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░▒▒░░░░░░▒▒▒▒░░\n░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░▒▒▒▒░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░\n░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░░░▒▒▒▒░░░░▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒░░▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"


for character_indexx in this_stringTwo:
   print(character_indexx, end = '')
   time.sleep(0.01)

print("Do you want Ice Cream?")

iceCream = input("")

if iceCream == "yes":
    this_stringThree = "help"
    
    for character_indexxx in this_stringThree:
        print(character_indexxx, end = '')
        time.sleep(0.01)

    for i in range(100):
        print("\n")
        time.sleep(0.01)

    sys.exit()

    

else:
    print("Awwww, that sucks! Well, cya next time!")
    time.sleep(2)
    sys.exit