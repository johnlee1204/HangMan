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
lines = lines.split("&newline&")
linesString = ""
for word in lines:
    if word.find("_") != -1:
        for x in word:
            linesString += x + " "
        # linesString = linesString[0:len(linesString) - 1]
    else:
        print(word)
print(linesString)
print('\n')
print('Guess a letter: ')

while 1:

    # Get letter from user
    print('\n')
    letter = input()

    # Sends letter
    letterBytes = letter.encode('utf-8')
    clientSocket.send(letterBytes)

    #Recieves newWord
    newWordInBytes = clientSocket.recv(1024)
    newWord = newWordInBytes.decode('utf-8')

    if newWord == "You have won the game":
        print("You Won!")
        clientSocket.close()
        input("Press Enter to continue...")
        exit()
    elif newWord == "You have lost the game":
        print("You Lost!")
        clientSocket.close()
        input("Press Enter to continue...")
        exit()
    elif newWord.find("Wrong, Next Player\'s turn!") != -1:
        print(newWord)
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