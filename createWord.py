import random
import string

def getNewWord():
    wordLength = random.randint(3, 10)
    word =  ''.join(random.choice(string.ascii_letters) for x in range(wordLength)). lower()
    addToList(word)
    return word

def addToList(word):
    with open('words.txt', "a+") as wordsFile:
        if word not in wordsFile:
                wordsFile.write(word + "\n")
    return 0


