# AP Computer Science Project 
# WORDLE GAME

# This section explains the instructions to the user before playing the game. 

def game_instruction():
    print("""Wordle is a single player game that requires the user to guess a five letter word that is hidden.
    
⦿  A player has to guess a five letter hidden word.

⦿  You have six attempts 

⦿  Your Progress Guide "✔❌❌✔⚠":

    "✔" Indicates that the letter at that position was guessed correctly 
    "⚠" indicates that the letter at that position is in the hidden word, but in a different position 
    "❌" indicates that the letter at that position is wrong, and isn't in the hidden word.

Enough said, Good Luck! 
""")


game_instruction()

# This section sets a list of random 5 letter words. It defines the word random and takes a random word from the list and sets it as random_word which is the same as the hidden_word.

def repeat_check_word():
  check_word()
def check_word():
  import random
  a_list = ['adopt', 'abyss', 'adore', 'adorn', 'adult', 'adobe', 'above', 'adapt', 'apple', 'bacon', 'skies', 'about', 'dolls', 'falls', 'miami', 'seize', 'serve', 'sharp', 'shine', 'shelf', 'slice', 'solid', 'space', 'abuse', 'adult','agent', 'anger', 'apple', 'award', 'basis', 'beach', 'birth', 'blood', 'board', 'brain', 'bread', 'brown', 'buyer', 'cause', 'chain', 'chair', 'chest', 'chief']
  
# Number of attempts are set at 6. A while loop is created to let the computer know that as long as you have more than 0 attempts you can continue guessing.

# "If" statemtent created to match the hidden word. Meaning, if the guess matches the hidden word then a congratulations message will be printed to ler the user know they guessed the word correcty.
  
  random_word = random.choice(a_list) 
  hidden_word = random_word
  attempt = 6
  while attempt > 0:
    guess = str(input("Guess the word: "))
    if guess == hidden_word:
      print("You guessed the words correctly! WIN 🕺🕺🕺 ")
      print("""Restart? Type yes or no:""")
      break
      
    else:
      attempt = attempt - 1
      print(f"you have {attempt} attempt(s) ,, \n ")
      for char, word in zip(hidden_word, guess):
            if word in hidden_word and word in char:
                print(word + " ✔ ")

            elif word in hidden_word:
                print(word + " ⚠ ")
            else:
                print(" ❌ ")
      if attempt == 0:
        print(" Game over !!!! ")
        print("""Restart? Type yes or no:""")
        break

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


if restart == str("yes"):
  import os
  os.system('clear')

if restart == str("no"):
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
