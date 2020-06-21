import sys

# Import socket library
from socket import *

if sys.argv.__len__() != 3:
    serverName = 'localhost'
    serverPort = 5895
# Get from command line
else:
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])

# Choose SOCK_STREAM, which is TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to server using hostname/IP and port
clientSocket.connect((serverName, serverPort))

#Recieves lines of words
linesInBytes = clientSocket.recv(1024)
lines = linesInBytes.decode('utf-8')
linesString = ""
for x in lines:
    linesString += x + " "
# linesString = linesString[0:len(linesString) - 1]
print(linesString)

while 1:

    # Get letter from user
    print('\n')
    letter = input('Guess a letter: ')

    # Sends letter
    letterBytes = letter.encode('utf-8')
    clientSocket.send(letterBytes)

    #Recieves newWord
    newWordInBytes = clientSocket.recv(len(linesInBytes))
    newWord = newWordInBytes.decode('utf-8')

    if newWord.find("_"):

        linesString = ""
        for x in newWord:
            linesString += x + " "
        # linesString = linesString[0:len(linesString) - 1]
    else:
        linesString = newWord

    print(newWord)
    if(linesString == 'You have won the game'):
        print(newWord)
        clientSocket.close()
        break