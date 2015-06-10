# Luke Miles, January 2015
import random
stresses = {'AA1', 'AE1', 'AH1', 'AO1', 'AW1', 'AY1', 'EH1', 'ER1', 'EY1', 'IH1', 'IY1', 'OW1', 'OY1', 'UH1', 'UW1'}

with open("phodict.txt") as fille:
    phodict = dict()
    for line in fille:
        words = line.split()
        phodict[words[0]] = tuple(words[1:])

def sle(lst, sublst):
    """ sublistexists """
    n = len(sublst)
    return any((sublst == lst[i:i+n]) for i in xrange(len(lst)-n+1))

def dr(w1, w2):
    """ doesrhyme """
    p1, p2 = phodict[wq], phodict[w2]
    if sle(p1, p2) or sle(p2, p1):
        return False
    for ind,sound in enumerate(reversed(p1)):
        if sound in stresses:
            break
    return p1[-ind-1:] == p2[-ind-1:]

def hms(w):
    """ how many syllables """
    p = phodict[w]
    return sum((sound[0] in "AEIOU") for sound in p)

def msm():
    """ make syllable map """
    dictt = {i:set() for i in xrange(0,15)}
    for word in phodict.iterkeys():
        dictt[hms(word)].add(word)
    return dictt

syldict = msm()

def gr(w):
    """ get rhymes """
    p = phodict[w]
    for ind,sound in enumerate(reversed(p)):
        if sound in stresses:
            p_end = p[-ind-1:]
            break
    yielded = set()
    for w2 in phodict.iterkeys():
        p2 = phodict[w2]
        if p_end != p2[-ind-1:]:
            continue
        if sle(p, p2) or sle(p2, p):
            continue
        if p2 in yielded:
            continue
        yielded.add(p2)
        yield w2

def gnsw(n):
    """ grab n syllable word """
    return random.sample(syldict[n], 1)[0]

def limerick():
    """ 10A,10A,6B,6B,10A """
    e1 = gnsw(1) # ending 1
    r1 = tuple(gr(e1))
    e2 = random.choice(r1)
    e5 = random.choice(r1)
    e3 = gnsw(1)
    r3 = tuple(gr(e3))
    e4 = random.choice(r3)
    l1 = ' '.join(gnsw(4) for _ in xrange(2)) + ' ' + e1
    l2 = ' '.join(gnsw(4) for _ in xrange(2)) + ' ' + e2
    l5 = ' '.join(gnsw(4) for _ in xrange(2)) + ' ' + e5
    l3 = ' '.join(gnsw(3) for _ in xrange(1)) + ' ' + e3
    l4 = ' '.join(gnsw(3) for _ in xrange(1)) + ' ' + e4
    return '\n'.join((l1,l2,l3,l4,l5))

