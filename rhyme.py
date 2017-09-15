# Luke Miles, September 2017
# Python 3
# TODO: update the other files in this directory

import random

STRESSES = {'AA1', 'AE1', 'AH1', 'AO1', 'AW1', 'AY1', 'EH1', 'ER1', 'EY1', 'IH1', 'IY1', 'OW1', 'OY1', 'UH1', 'UW1'} # set of all stressed vowel sounds

def fileToDict(filepath):
    dictA = dict()
    with open(filepath) as fileA:
        for line in fileA:
            words = line.split() # splits the line on any whitespace
            dictA[words[0]] = tuple(words[1:])
    return dictA

PHODICT = fileToDict("phodict.txt") # phonetic dictionary

def isSubList(listA, listB):
    "returns whether or not one list contains the other"
    if len(listA) < len(listB):
        return isSubList(listB, listA)
    n = len(listB)
    for start in range(len(listA)-n+1):
        if all(listA[start+i] == listB[i] for i in range(n)):
            return True
    return False

def isRhyme(wordA, wordB):
    "returns whether or not word1 and word2 rhyme"
    soundsA, soundsB = PHODICT[wordA], PHODICT[wordB]
    if isSubList(soundsA, soundsB):
        # you don't want pickle to rhyme with superpickle
        return False
    for index,sound in enumerate(reversed(soundsA)):
        if sound in STRESSES:
            break
    return p1[-index-1:] == p2[-index-1:]

def syllableCount(word):
    "returns the number of syllables in word"
    sounds = PHODICT[word]
    return sum(int(sound[0] in "AEIOU") for sound in sounds)

def makeSyllableMap():
    """returns a dictionary where a key is a number of syllables and its value
    is the set of all words with that many syllables"""
    dictA = {i: set() for i in range(0,15)}
    for word in PHODICT.keys():
        dictA[syllableCount(word)].add(word)
    return dictA

SYLDICT = makeSyllableMap()

def getRhymes(word):
    "yields all words that rhyme with word"
    sounds = PHODICT[word]
    for index,sound in enumerate(reversed(sounds)):
        if sound in STRESSES:
            ending = sounds[-index-1:]
            break
    yielded = set()
    for wordB, soundsB in PHODICT.items():
        if (ending == soundsB[-index-1:]) and (soundsB not in yielded) and (not isSubList(sounds, soundsB)):
            yielded.add(soundsB)
            yield wordB

def findWord(n):
    "returns a random n syllable word"
    return random.sample(SYLDICT[n], 1)[0]

def makeLimerick():
    "rhyme pattern: 10A,10A,6B,6B,10A "
    e1 = findWord(1) # e1 is short for ending 1
    r1 = tuple(getRhymes(e1))
    e2 = random.choice(r1)
    e5 = random.choice(r1)
    e3 = findWord(1)
    r3 = tuple(getRhymes(e3))
    e4 = random.choice(r3)
    lines = [[findWord(4), findWord(4), e1],
             [findWord(4), findWord(4), e2],
             [findWord(3), e3],
             [findWord(3), e4],
             [findWord(4), findWord(4), e5]]
    return '\n'.join(' '.join(line) for line in lines)
