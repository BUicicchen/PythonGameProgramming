def readTxt(filepath):
    '''Reads and return a text in a file
    :param filepath: address to the input file
    :return: list
    '''
    #return 0.0

    #Reads a file and returns it in a list
    f = open(filepath,'r')
    returnText = f.read().lower()
    f.close()
    return returnText.split()

def findNextWord(word, text):
    '''Find all the words that happen next the given word.
    :param word: word of interest
    :param text: the text to study
    :return: a list with the nextwords
    '''
    nextWord = []
    frequency = []
    for idx, wrd in enumerate(text):
        if wrd == word:
            #find the next words
            nxtwrd = text[idx+1]
            if nxtwrd in nextWord:
                #find the occurance of each of the next word, add 1 to frequency
                frequency[nextWord.index(nxtwrd)]+=1
            else:
                #if not, then the nextword has the frequency of 1
                nextWord.append(nxtwrd)
                frequency.append(1)
    #nextWord, frequency = 0.0, 0.0
    return nextWord, frequency

def probOccurrence(count):
    """Calculates the accumulated probability of an event
   :param count: a list with event's count
   :return: a list with probabilities
   """

    nEvents = sum(count)
    prob = [1.0*x/nEvents for x in count]
    density = []
    total = 0
    for p in prob:
       total += p
       density.append(total)
    return density

def randomWord(words, density):
    """Randomly picks a word from the list of the next occurrence that is given a density value
    :param words: random words that are picked
    :param density: the probability of the occurrence of each next words
    :return: a list of words that are picked
    """
    import random as rn
    n = rn.random()
    idx = 0
    while n > density[idx]:
        idx += 1
    return words[idx]
