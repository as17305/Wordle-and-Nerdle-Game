from os.path import dirname, join

words = None
current_dir = dirname(__file__)
file_path = join(current_dir, 'word_list.txt')
with open(file_path, 'r') as reader:
#Read in the word list from the dictionary.txt file
    words = reader.read()
#Convert words from a string to a list
#by splitting over new lines \n
words = words.split("\n")
word_five = []
for i in range(len(words)):
  if len(words[i]) == 5:
    word_five.append(words[i].lower())
import random
random = random.randint(0, len(word_five) - 1)
secretWord = word_five[random]
print("Guess five letter word in six tries.")
for i in range(6):
  guess = input(f"Try #{i + 1}: Guess the word\n")
  if guess == secretWord:
      print(f"Nice job! You got it in {i + 1} tries.")
      break
  if guess not in words:
      print(f"{guess} is not a real word")
  elif not(len(guess) == 5):
      print(f"{guess} is not a five letter word")
  else:
    for i in range(5):
     if guess[i] == secretWord[i]:
        print(f"{guess[i]} is in the word and in the correct spot.")
     elif guess[i] in secretWord and not(guess[i] == secretWord[i]):
        print(f"{guess[i]} is in the word but in the wrong spot.")
     else:
        print(f"{guess[i]} is not in the word in any spot.")
  if i == 5:
      print(f"Here's the (not so) secret word you are trying to guess: {secretWord}")
      print("You lose :-(")