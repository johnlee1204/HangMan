import sys

# Import socket library
from socket import *

if sys.argv.__len__() != 3:
    serverName = '192.168.1.15'
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
print('\n')
print('Guess a letter: ')

while 1:

    # Get letter from user
    print('\n')
    letter = input()
    print('\n')
    # Sends letter
    letterBytes = letter.encode('utf-8')
    clientSocket.send(letterBytes)

    #Recieves newWord
    newWordInBytes = clientSocket.recv(1024)
    newWord = newWordInBytes.decode('utf-8')
    newWords = newWord.split("&newline&")

    linesString = ""
    for word in newWords:
        if word.find("_") != -1:
            for x in word:
                linesString += x + " "
            # linesString = linesString[0:len(linesString) - 1]
        else:
            print(word)
    print(linesString)
    if linesString == "":
        print("You Won!")
        # clientSocket.close()