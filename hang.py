import random
HANGMANPICS = ['''
  3.
  4.   +---+
  5.   |   |
  6.       |
  7.       |
  8.       |
  9.       |
 10. =========''', '''
 11.
 12.   +---+
 13.   |   |
 14.   O   |
 15.       |
 16.       |
 17.       |
 18. =========''', '''
 19.
 20.   +---+
 21.   |   |
 22.   O   |
 23.   |   |
 24.       |
 25.       |
 26. =========''', '''
 27.
 28.   +---+
 29.   |   |
 30.   O   |
 31.  /|   |
 32.       |
 33.       |
 34. =========''', '''
 35.
 36.   +---+
 37.   |   |
 38.   O   |
 39.  /|\  |
 40.       |
 41.       |
 42. =========''', '''
 43.
 44.   +---+
 45.   |   |
 46.   O   |
 47.  /|\  |
 48.  /    |
 49.       |
 50. =========''', '''
 51.
 52.   +---+
 53.   |   |
 54.   O   |
 55.  /|\  |
 56.  / \  |
 57.       |
 58. =========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra christina'.split()

def getRandomWord(wordList):
      # This function returns a random string from the passed list of strings.
     wordIndex = random.randint(0, len(wordList) - 1)
     return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
      print(HANGMANPICS[len(missedLetters)])
      print()

      print('Missed letters:', end=' ')
      for letter in missedLetters:
          print(letter, end=' ')
      print()

      blanks = '_' * len(secretWord)

      for i in range(len(secretWord)): # replace blanks with correctly guessed letters
          if secretWord[i] in correctLetters:
              blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

      for letter in blanks: # show the secret word with spaces in between each letter
          print(letter, end=' ')
      print()

def getGuess(alreadyGuessed):
      # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
      while True:
          print('Guess a letter.')
          guess = input()
          guess = guess.lower()
          if len(guess) != 1:
              print('Please enter a single letter.')
          elif guess in alreadyGuessed:
              print('You have already guessed that letter. Choose again.')
          elif guess not in 'abcdefghijklmnopqrstuvwxyz':
              print('Please enter a LETTER.')
          else:
             return guess

def playAgain():
     # This function returns True if the player wants to play again, otherwise it returns False.
     print('Do you want to play again? (yes or no)')
     return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
     displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

     # Let the player type in a letter.
     guess = getGuess(missedLetters + correctLetters)

     if guess in secretWord:
         correctLetters = correctLetters + guess

         # Check if the player has won
         foundAllLetters = True
         for i in range(len(secretWord)):
             if secretWord[i] not in correctLetters:
                 foundAllLetters = False
                 break
         if foundAllLetters:
             print('Yes! The secret word is "' + secretWord + '"! You have won!')
             gameIsDone = True
     else:
         missedLetters = missedLetters + guess

         # Check if player has guessed too many times and lost
         if len(missedLetters) == len(HANGMANPICS) - 1:
             displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
             print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
             gameIsDone = True

     # Ask the player if they want to play again (but only if the game is done).
     if gameIsDone:
         if playAgain():
             missedLetters = ''
             correctLetters = ''
             gameIsDone = False
             secretWord = getRandomWord(words)
         else:
             break