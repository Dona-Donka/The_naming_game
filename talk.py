import random
import createWord
import getData



def checkWord(speaker, hearer, successes):
    if len(speaker) != 0:
        word = random.choice(speaker)
        if word in hearer:
            success(speaker, hearer, word)
            successes = getData.updateTotalSuccesses(successes)
        else:
            failrue(hearer, word)
    else:
        speaker.append(createWord.getNewWord())
    return successes


def success(speaker, hearer, word):
    speaker = [word]
    hearer = [word]
    return speaker, hearer


def failrue(hearer, word):
    hearer.append(word)
    return hearer