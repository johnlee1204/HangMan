import sys
import random

# Import socket library
from socket import *

wordlist = []
guessedCharacters = []



def answerSection(word):
    answerSectionString = ""
    for letter in word:
        try:
            index = guessedCharacters.index(letter)
            answerSectionString += letter
        except ValueError:
            answerSectionString += "_"
    return answerSectionString.find("_")


def guessLetter(character):
    try:
        guessedCharacters.index(character)
        return "duplicate guess"
    except ValueError:
        guessedCharacters.append(character)

    if word.find(character) == -1:
        return "guess again"
    else:
        return "correct"

def selectWordFromWordlist():
    return wordlist[int(random.random()*1000)]

def putWordsInWordlist():
    with open('wordList.txt','r') as file:
        for word in file:
            wordlist.append(word)


if sys.argv.__len__() != 2:
    serverPort = 5895
# Get port number from command line
else:
    serverPort = int(sys.argv[1])

# Choose SOCK_STREAM, which is TCP
# This is a welcome socket
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Start listening on specified port
serverSocket.bind(('', serverPort))

# Listener begins listening
serverSocket.listen(1)

print("The server is ready to receive")

#Set secret word
putWordsInWordlist()
word = selectWordFromWordlist()
word = word[0:len(word) - 1]
print(word)
linesForString = ''
#Prints out number of letters
for x in word:
    linesForString += '_'

newWord = word

# Wait for connection and create a new socket
# It blocks here waiting for connection
clients = []
# connectionSocket, addr = serverSocket.accept()
while len(clients) != 2:
    connectionSocket, addr = serverSocket.accept()
    clients.append(connectionSocket)
    print("New Client! # " + str(len(clients) - 1))

win = ' '
#Sends lines of words
x = len(word)
numberOfTries = int((1/x) * 30 + 3)

print("First Player is Client: " + str(numberOfTries % 2))
linesInBytes = linesForString.encode('utf-8')
clients[numberOfTries % 2].send(linesInBytes)

lose = 0


while 1:


    l = list(word)
    list2 = list(linesForString)

    win = False

    while 1:

        while win == False:
            increment = True
            # Receives Letter
            letter = clients[numberOfTries % 2].recv(1024)
            letterString = letter.decode('utf-8')
            print(letterString)

            guessLetterResult = guessLetter(letterString)
            messageForUser = ""
            if guessLetterResult == "duplicate guess":
                messageForUser += "hey retard guess again&newline&"
                increment = False
            elif guessLetterResult == "guess again":
                messageForUser += "Wrong, Next Player\'s turn!"
                clients[numberOfTries % 2].send(messageForUser.encode('utf-8'))
                messageForUser = ""
            elif guessLetterResult == "correct":
                messageForUser += "Correct!&newline&"
                increment = False
            #Sends newWord

            if increment:
                numberOfTries -= 1

            messageForUser += ("Guess a Character, you have " + str(numberOfTries) + " attempt(s) left. You have guessed: " + " ".join(guessedCharacters) + "&newline&")

            answerSectionString = ""
            for letter in word:
                try:
                    index = guessedCharacters.index(letter)
                    answerSectionString += letter
                except ValueError:
                    answerSectionString += "_"

            messageForUser += answerSectionString

            if answerSectionString.find("_") == -1:
                win = True
                winGame = 'You have won the game'
                winGameInBytes = winGame.encode('utf-8')

                lostGame = 'You have lost the game'
                lostGameInBytes = lostGame.encode('utf-8')


                clients[numberOfTries % 2].send(winGameInBytes)
                clients[(numberOfTries+1) % 2].send(lostGameInBytes)
                clients[0].close()
                clients[1].close()
                exit()
            else:
                print(messageForUser)
                messageForUserBytes = messageForUser.encode('utf-8')
                clients[numberOfTries % 2].send(messageForUserBytes)

        break
    break