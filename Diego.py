# AP Computer Science Project 
# WORDLE GAME

# This section explains the instructions to the user before playing the game. 

def game_instruction():
    print("""Wordle is a single player game that requires the user to guess a five letter word that is picked randomly out of a list of five letter words. 
    
The instructions are below!

┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
    
‣‣  A player has to guess a five letter hidden word.

‣‣  You have six attempts 

‣‣  Your Progress Guide "✔❌❌✔⚠":

    "✔" Indicates that the letter at that position was guessed correctly
    
    "⚠" indicates that the letter at that position is in the hidden word, but in a different position.
    
    "❌" indicates that the letter at that position is wrong, and isn't in the hidden word.

Enough said, Good Luck! 
""")


game_instruction()

# This section sets a list of random 5 letter words. It defines the word randomly and takes a random word from the list and sets it as random_word which is the same as the hidden_word.

def repeat_check_word():
  check_word()
def check_word():
  import random
  a_list = ['adopt', 'abyss', 'adore', 'adorn', 'adult', 'adobe', 'above', 'adapt', 'apple', 'bacon', 'skies', 'about', 'dolls', 'falls', 'miami', 'seize', 'serve', 'sharp', 'shine', 'shelf', 'slice', 'solid', 'space', 'abuse', 'adult','agent', 'anger', 'apple', 'award', 'basis', 'beach', 'birth', 'blood', 'board', 'brain', 'bread', 'brown', 'buyer', 'cause', 'chain', 'chair', 'chest', 'chief', 'dolls', 'loafs', 'water', 'flare', 'threw', 'polls', 'round', 'plant', 'roots', 'crops', 'house']
  
# Number of attempts are set at 6. A while loop is created to let the computer know that as long as you have more than 0 attempts you can continue guessing.

# "If" statemtent created to match the hidden word. Meaning, if the guess matches the hidden word then a congratulations message will be printed to ler the user know they guessed the word correcty.
  
  random_word = random.choice(a_list) 
  hidden_word = random_word
  attempt = 6
  while attempt > 0:
    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
    guess = str(input("Guess the word: "))
    print("")
    if guess == hidden_word:
      print("You guessed the words correctly! WIN 🕺🕺🕺 ")
      print("""Restart? Type yes or no:""")
      break

    else:
      attempt = attempt - 1
      print(f"...you have {attempt} attempt(s):\n ")
      
      # Defined "owo" and set the rules for when thw word is guessed and what happens to each word.
      
      uwu = ""
      owo = ""
      for char, word in zip(random_word, guess):
          if word in random_word and word in char:

              # Used += to assign the new value to the variable and add it to the same line. This way I was able to make the line horizontally instead of vertically which is what happened with the previous code I had.
              
              # Assigned ASCII code colors to each letter depending on its accuracy (correct = green, partial = yellow, wrong = red)
              owo += "\033[32m✔\t"
              uwu += "\033[32m{letter} \t".format(letter=word)
          elif word in random_word:
              owo += "\033[33m⚠\t"
              uwu += "\033[33m{letter} \t".format(letter=word)
          else:
              owo += "\033[31m❌\t"
              uwu += "\033[31m{letter} \t".format(letter=word)
      uwu.expandtabs(4)
      guess = uwu

      # When the user enters a word, the word is then analyzed based on the previous if's, elif's, else's. "owo" is printed based on the standards.

      # Also, the user's guessed word and color reset is printed below the "owo" output.

      print(owo)
      print(guess + "\033[0m")
# When the number of attempts reaches 0, the user is not able to guess anymore. "Game Over!!, the word was:" and the hidden word is now revealed using the print(random_word) command.

#The user is then asked a question weather or not they would like to continue playing by inputing either yea or no. Based on those inputs, the code has an option in which the game either ends and clears everything or the game restarts and new game is started again.
      
      if attempt == 0:
        print("")
        print("Game Over!!") 
        print("The word was:")
        print("┈┈┈┈┈")
        print(random_word)
        print("┈┈┈┈┈")
        print("""Restart? Type yes or no:""")
        break
        
# Check_word() function is called to be executed.
        
check_word()

def end_game():
  import os
  os.system('clear')

restart = input("")

if restart == str("yes"):
  import os
  os.system('clear')

if restart == str("no"):
  end_game()

# New game instructions are created to keep the user more engaged, and it makes the game more interesting since the user is now interacting with the computer.
  
def game_instructions():
  print("""Welcome back fellow wordle players!
    
The word is different this time!

Good Luck!

""")

game_instructions()
  
repeat_check_word()

restart = input("")

if restart == str("yes"):
  import os
  os.system('clear')

if restart == str("no"):
  end_game()
  
def game_instructions():
  print("""Welcome back for the second time fellow wordle players!
    
The word is different from the last two games!

Good Luck, once again!

""")

game_instructions()
  
repeat_check_word()

restart = input("yes")

if restart == str("yes"):
  import os
  os.system('clear')
  
if restart == ("no"):
    end_game()

def game_instructions():
  print("""I dont have to tell you again...you are here for a reason...Good Luck!

""")

game_instructions()
  
repeat_check_word()

restart = input("")

if restart == str("yes"):
  import os
  os.system('clear')

if restart == str("no"):
  end_game()

def end_game():
  import os
  os.system('clear')
  print("""Thank you for playing! Come back soon...""")
  import os
  os.system('clear')

def game_instructions():
  print("""Are you guessing the words correctly or are you really bad at the game?

Good luck!

""")

game_instructions()
  
repeat_check_word()

restart = input("")

if restart == str("yes"):
  import os
  os.system('clear')

if restart == str("no"):
  end_game()
