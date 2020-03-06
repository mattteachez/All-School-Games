import random

def main():
    welcome = ['Welcome to Hangman! A word will be chosen at random and',
               'you must try to guess the word correctly letter by letter',
               'before you run out of attempts. Good luck!'
               ]


    for line in welcome:
        print(line, sep='\n')

    play_again = True

    while play_again:

        words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "crisps", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo",
                 "mouse","orange", "apple", "fork", "dummy", "mat",
                 "house", "keyboard", "tshirt", "monitor", "television",
                 "book", "badge", "pencil", "paper", "watch", "shoe",
                 "backpack", "bottle", "sweatpants", "printer"]

        chosen_word = random.choice(words).lower()
        player_guess = None 
        guessed_letters = []
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("_ ")
        joined_word = None 

        HANGMAN = (
            
"""
   ____
  |    |      
  |           Guessed : """ + str(guessed_letters) + """
  |           
  |    
  |   
 _|_
|   |______
|          |
|__________|
""",
"""
   ____
  |    |      
  |    o      Guessed : """ + str(guessed_letters) + """
  |           
  |    
  |   
 _|_
|   |______
|          |
|__________|
""",
"""
   ____
  |    |      
  |    o      Guessed : """ + str(guessed_letters) + """
  |    |      
  |    
  |   
 _|_
|   |______
|          |
|__________|
""",
"""
   ____
  |    |      
  |    o      Guessed : """ + str(guessed_letters) + """
  |   /|      
  |    
  |   
 _|_
|   |______
|          |
|__________|
""",
"""
   ____
  |    |      
  |    o      Guessed : """ + str(guessed_letters) + """
  |   /|\    
  |    
  |   
 _|_
|   |______
|          |
|__________|
""",
"""
   ____
  |    |      
  |    o      Guessed : """ + str(guessed_letters) + """
  |   /|\     
  |    |
  |   
 _|_
|   |______
|          |
|__________|
""",
"""
   ____
  |    |      
  |    o      Guessed : """ + str(guessed_letters) + """
  |   /|\     
  |    |
  |   /
 _|_
|   |______
|          |
|__________|
""",
"""
   ____
  |    |      
  |    o      Guessed : """ + str(guessed_letters) + """
  |   /|\     
  |    |
  |   / \
 _|_
|   |______
|          |
|__________|
""")

        print(HANGMAN[0])
        attempts = len(HANGMAN) - 1


        while (attempts != 0 and "_ " in word_guessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joined_word = "".join(word_guessed)
            print(joined_word)

            try:
                player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
            except: 
                print("That is not valid input. Please try again.")
                continue                
            else: 
                if not player_guess.isalpha(): 
                    print("That is not a letter. Please try again.")
                    continue
                elif len(player_guess) > 1: 
                    print("That is more than one letter. Please try again.")
                    continue
                elif player_guess in guessed_letters: 
                    print("You have already guessed that letter. Please try again.")
                    continue
                else:
                    pass
            
            guessed_letters += player_guess

            for letter in range(len(chosen_word)):
                if player_guess == chosen_word[letter]:
                    word_guessed[letter] = player_guess
                    print(HANGMAN[(len(HANGMAN) - 1) - attempts])

            if player_guess not in chosen_word:
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "_ " not in word_guessed: 
            print(("\nCongratulations! {} was the word").format(chosen_word))
        else: 
            print(("\nUnlucky! The word was {}.").format(chosen_word))

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            chosen_word = random.choice(words).lower()
            play_again = True

if __name__ == "__main__":
    main()

