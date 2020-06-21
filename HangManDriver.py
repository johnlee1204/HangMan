import random
wordlist = []
guessedCharacters = []
def drawHangMan():
    # TODO Draw the hangman using the current number of wrong guesses
    print("Hello")
def answerSection(word):
    answerSectionString = ""
    for letter in word:
        try:
            index = guessedCharacters.index(letter)
            answerSectionString += letter
        except ValueError:
            answerSectionString += "_"
    print(answerSectionString)
    return answerSectionString.find("_")


def guessLetter(character):
    if word.find(character) == -1:
        print("guess again")
    else:
        print("correct")
        guessedCharacters.append(character)
        return "correct"
    try:
        index = guessedCharacters.index(character)
        return "duplicate guess"
    except ValueError:
        guessedCharacters.append(character)

def listPastWrongGuesses():
    # TODO List all the wrong letters the user has guessed
    print("Hello")


def promptUserForLetterGuess():
    # TODO Get the users guess as a letter
    print("Hello")

def promptUserForAnswerGuess():
    # TODO Get the users guess the word
    print("Hello")

def selectWordFromWordlist():
    return wordlist[int(random.random()*1000)]

def putWordsInWordlist():
    # TODO Select a word from the words txt file for the user to guess
    with open('wordList.txt','r') as file:
        for word in file:
            wordlist.append(word)

putWordsInWordlist()
word = selectWordFromWordlist()
word = word[0:len(word) - 1]
# print(word)
# print(len(word))


answerSection(word)
i = 0
x = len(word)
numberOfTries = int((1/x) * 30 + 3)
if numberOfTries > 15:
    numberOfTries = 15
while i < numberOfTries:
    print("Guess a Character, you have " + str(numberOfTries - i) + " attempt(s) left. You have guessed: " + " ".join(guessedCharacters))
    characterGuess = input()
    guessLetterResult = guessLetter(characterGuess)

    if guessLetterResult == "duplicate guess":
        print("hey retard guess again")
        continue
    elif guessLetterResult == "correct":
        i = i - 1
    if answerSection(word) == -1:
        print("you win!")
        break
    if i == numberOfTries - 1:
        print("you lost!")
    i += 1
print(word)