import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


print(logo,"\n")

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["mumbai", "pune", "solapur", "dharashiv", "nashik"]

choosen_word = random.choice(word_list)

print("Guess the popular cities in Maharashtra. \n")

display = []
for letter in choosen_word:
        display += "_"

disp = " ".join(display)
print("***", disp, "***")

lives = 6

end_of_game = False

while not end_of_game:
    user_guess = input("Guess the word: \n").lower()

    for position in range(len(choosen_word)):
        if choosen_word[position] == user_guess:
            display[position] = user_guess
            
    if user_guess not in choosen_word:
         lives -= 1
         print(f"You have {lives} left.")
         print(stages[lives])
         if lives == 0:
              end_of_game = True
              print("You loose the game :( \n")
              print(f"You have {lives} left.")
              print("The choosen word was: ", choosen_word)

    disp = " ".join(display)
    print("***", disp, "***")

    if "_" not in display:
        end_of_game = True
        print(f"You have {lives} left.")
        print("You win the game ! \n")

