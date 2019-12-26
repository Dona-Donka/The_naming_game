import random
import string

def getNewWord():
    wordLength = random.randint(3, 10)
    word =  ''.join(random.choice(string.ascii_letters) for x in range(wordLength)). lower()
    return word

