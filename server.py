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
    print(answerSectionString)
    return answerSectionString.find("_")


def guessLetter(character):
    try:
        guessedCharacters.index(character)
        return "duplicate guess"
    except ValueError:
        guessedCharacters.append(character)

    if word.find(character) == -1:
        print("guess again")
    else:
        print("correct")
        guessedCharacters.append(character)
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
connectionSocket, addr = serverSocket.accept()
win = ' '
#Sends lines of words
linesInBytes = linesForString.encode('utf-8')
connectionSocket.send(linesInBytes)

lose = 0
while 1:


    l = list(word)
    list2 = list(linesForString)

    win = False

    while 1:

        while win == False:
            losee = 0
            # Receives Letter
            letter = connectionSocket.recv(1024)
            letterString = letter.decode('utf-8')
            print(letterString)

            guessLetterResult = guessLetter(letterString)
            messageForUser = ""
            if guessLetterResult == "duplicate guess":
                messageForUser += "hey retard guess again"

            #Sends newWord

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
                connectionSocket.send(winGameInBytes)
                connectionSocket.close()
            else:
                messageForUserBytes = messageForUser.encode('utf-8')
                connectionSocket.send(messageForUserBytes)

        break
    break