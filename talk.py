import random
import createWord
import getData

def checkWord(speaker, hearer, successes):
    if len(speaker) != 0:
        word = random.choice(speaker)
        if word in hearer:
            success(speaker, hearer, word, successes)
        else:
            failrue(hearer, word)
    else:
        speaker.append(createWord.getNewWord())


def success(speaker, hearer, word, successes):
    speaker = [word]
    hearer = [word]
    successes = successes + 1
    print("success", successes)
    return speaker, hearer, successes

def failrue(hearer, word):
    hearer.append(word)
    return hearer