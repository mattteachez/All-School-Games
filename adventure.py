import time

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
sword = 0
flower = 0

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

#Restarting script
def restart():
    reDo = '''\nYou see a pretty woman comming towards you...
You examine your surrounding at realise you don't
know where you are. You look up to be greeted by the
womans beautiful face. She smiles at you, as her
silver hair blew in the wind. A sharp pain started
piercing your unprepared heart. You winced and fell
to your knees, now screaming. You open your eyes, jolt
up and look around you. A serious feeling of dejavu hits
you, as you see a huge running goblin, heading your way{}'''.format("\n")

    for text in reDo:
        print(text, end = '')
        time.sleep(0.03)

    story()

#The story is broken into sections, starting with "intro"
def intro():
    storyOne = '''After a drunken night out with friends, you awaken the
next morning in a thick, dank forest. Head spinning and 
fighting the urge to vomit, you stand and marvel at your new
ufamiliar setting. The peace quickly fades when you hear a
grotesque sound emitting behind you. A slobbering goblin,
an abnormally large one at that, is running towards you.
You will:'''

    for text in storyOne:
        print(text, end = '')
        time.sleep(0.03)
  
    time.sleep(3)

    story()

def story():
    choiceOne = ' \n\nA. Grab a nearby rock and throw it at the goblin '
    time.sleep(1)
    choiceTwo = '\nB. Lie down and wait to be mauled'
    time.sleep(1)
    choiceThree = '\nC. Run'

    for text in choiceOne:
        print(text, end = '')
        time.sleep(0.01)

    for text in choiceTwo:
        print(text, end = '')
        time.sleep(0.01)

    for text in choiceThree:
        print(text, end = '')
        time.sleep(0.01)
    
    choice = input("\n>>> ")
    
    if choice in answer_B:
        diedZero = '''\nThe goblin smashes your head
\n\nYou died!'''
        
        for text in diedZero:
            print(text, end = '')
            time.sleep(0.03)
            
        restart()

    elif choice in answer_A:
        option_rock()
        
    elif choice in answer_C:
        option_run()
        
    else:
        print (required)
        intro()

def option_rock():
    storyTwo = '''\nThe goblin is stunned, but regains control. He begins
running towards you again. Will you:'''

    for text in storyTwo:
        print(text, end = '')
        time.sleep(0.03)
        
    time.sleep(1)
    choiceOneOne = '\nA. Run'
    time.sleep(1)
    choiceTwoOne = '\nB. Throw a rock'
    time.sleep(1)    
    choiceThreeOne = '\nC. Run towards a nearby cave'

    for text in choiceOneOne:
        print(text, end = '')
        time.sleep(0.01)

    for text in choiceTwoOne:
        print(text, end = '')
        time.sleep(0.01)

    for text in choiceThreeOne:
        print(text, end = '')
        time.sleep(0.01)
    
    choice = input("\n>>> ")
    
    if choice in answer_A:
        option_run()
        
    elif choice in answer_B:
        diedOne = '''\nYou decided to throw another rock, as if the first  
        rock thrown did much damage. The rock flew well over the 
        goblins head. You missed. \n\nYou died!'''

        for text in diedOne:
            print(text, end = '')
            time.sleep(0.03)

    elif choice in answer_C:
        option_cave()

    restart()

def option_cave():
    storyThree = '''\nYou were hesitant, since the cave was dark and 
ominous. Before you fully enter, you notice a shiny sword on 
the ground. Do you pick up a sword. Y/N?'''

    for text in storyThree:
        print(text, end = '')
        time.sleep(0.03)
    
    choice = input("\n>>> ")
    
    if choice in yes:
        sword = 1
        
    else:
        sword = 0
        
    continuationTextOne = '\nWhat do you do next?'

    for text in continuationTextOne:
        print(text, end = '')
        time.sleep(0.03)
        
    time.sleep(1)
    
    choiceOneTwo = '\nA. Hide in silence'
    time.sleep(1)
    choiceTwoTwo = '\nB. Fight'
    time.sleep(1)
    choiceThreeTwo = '\nC. Run'
    

    for text in choiceOneTwo:
        print(text, end = '')
        time.sleep(0.01)

    for text in choiceTwoTwo:
        print(text, end = '')
        time.sleep(0.01)

    for text in choiceThreeTwo:
        print(text, end = '')
        time.sleep(0.01)
    
    choice = input("\n>>> ")
    
    if choice in answer_A:
        diedTwo = '''\nReally? You're going to hide in the dark? I think 
goblins can see very well in the dark, right? Not sure, but 
I'm going with YES, so...\n\nYou died!'''

        for text in diedTwo:
            print(text, end = '')
            time.sleep(0.03)
        
    elif choice in answer_B:
        if sword > 0:
            normalEnding = '''\nYou laid in wait. The shimmering sword attracted 
the goblin, which thought you were no match. As he walked 
closer and closer, your heart beat rapidly. As the goblin 
reached out to grab the sword, you pierced the blade into 
its chest. \n\nYou survived!'''
            
            for text in normalEnding:
                print(text, end = '')
                time.sleep(0.03)
            
        
        elif sword < 0:
             diedThree = '''\nYou should have picked up that sword. You're 
defenseless! You where inevitably cornered, and killed
you died!'''

             for text in diedThree:
                 print(text, end = '')
                 time.sleep(0.03)


             restart()

    elif choice in answer_C:
        continuationTextTwo = '''As the goblin enters the dark cave, you sliently 
sneak out. You're several feet away, but the goblin turns 
around and sees you running.'''
         
        for text in continuationTextTwo:
            print(text, end = '')
            time.sleep(0.03)

        option_run()
           
    else:
        print (required)
        option_cave()

def option_run():
    continuationTextTwoPointO = """\nYou run as quickly as possible, but the goblin's 
    speed is too great. You will:"""

    for text in continuationTextTwoPointO:
            print(text, end = '')
            time.sleep(0.03)

    time.sleep(1)
    
    choiceOneThree = '\nA. Hide behind boulder'
    time.sleep(1)
    choiceTwoThree = '\nB. Trapped, so you fight'
    time.sleep(1)
    choiceThreeThree = '\nC. Run towards an abandoned town'
    time.sleep(1)

    for text in choiceOneThree:
        print(text, end = '')
        time.sleep(0.01)

    for text in choiceTwoThree:
        print(text, end = '')
        time.sleep(0.01)

    for text in choiceThreeThree:
        print(text, end = '')
        time.sleep(0.01)
    
    choice = input("\n>>> ")
    
    if choice in answer_A:
        diedFour = """You're easily spotted. 
        \n\nYou died!"""
        
        for text in diedFour:
                 print(text, end = '')
                 time.sleep(0.03)
                 
        restart()
        
    elif choice in answer_B:
        diedFive = """\nYou're no match for an goblin. 
        \n\nYou died!"""

        for text in diedFive:
                 print(text, end = '')
                 time.sleep(0.03)
                 
        restart()
        
    elif choice in answer_C:
        option_town()
        
    else:
        print(required)
        option_run()
    
def option_town():
    yesNoOne = '''\nWhile frantically running, you notice a rusted "
sword lying in the mud. You quickly reach down and grab it, 
but miss. You try to calm your heavy breathing as you hide 
behind a delapitated building, waiting for the goblin to come 
charging around the corner. You notice a purple flower 
near your foot. Do you pick it up? Y/N'''

    for text in yesNoOne:
            print(text, end = '')
            time.sleep(0.03)
    
    choice = input("\n>>> ")
    
    if choice in yes:
        flower = 1
    else:
        flower = 0
        continuationTextThree = '''You hear its heavy footsteps and ready yourself for "
        "the impending goblin.'''
        time.sleep(1)

        for text in continuationTextThree:
            print(text, end = '')
            time.sleep(0.03)
        
    if flower > 0:
        happyEnding = '''\nYou quickly hold out the purple flower, somehow 
hoping it will stop the goblin. It does! The goblin was looking 
for love. This got weird, but you survived! \nAfter a night of
squeaking the bed, you wake up. \nThe goblin is pregnant! You now
have years of happiness ahead of you!!'''

        for text in happyEnding:
            print(text, end = '')
            time.sleep(0.03)        
    else:
        diedSix = """\nMaybe you should have picked up the flower. 
        \n\nYou died!"""
        
        restart()

        for text in diedSix:
            print(text, end = '')
            time.sleep(0.03)
        
intro()
