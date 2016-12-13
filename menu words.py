'''This program lists out all unique words in an article and prints out how many time the word appears'''

import urllib.request
#Python module for retrieving url pages

#url with the vocabulary of interest
req = urllib.request.Request('https://archive.org/stream/TheChroniclesOfNarnia/The%20Chronicles%20of%20Narnia_djvu.txt')
#open the url
response = urllib.request.urlopen(req)
#read the html file: DEcode using utf-8
the_page = response.read().decode("utf-8")

print(the_page)

glossary = the_page.split()

for w in glossary:
    if '<pre' in w:
        start = glossary.index(w)
        print(start)
    if '</pre' in w:
        finish = glossary.index(w)
        print(finish)


'''
for index, word in enumerate(narnya):
    lowerCase = word.lower()
    for character in lowerCase:
        if character in ['!.;:,"?/=>1234567890()-']:
            lowerCase.replace(character, '')
    narnya[index] = lowerCase.replace(character,'')
print(narnya)


'''


def printMenu(lwidth, rwidth, title, items):
    #prints out the word and its frequency of appearing
    """
    Prints a dictionary's keys and values in a menu format
    :param items: dictionary
    :param lwidth: int
    :param rwidth: int
    :param title: string
    :return: None
    """
    x = title
    print(x.center(lwidth+rwidth, "-"))
    for k, v in items.items():
        print(k.ljust(lwidth, ".") + str(v).rjust(rwidth, "."))
    return items

narnya = glossary[start:finish]
#convert words to lower case
lowerCase = [word.lower() for word in narnya]

#take out all punctuations
for word in lowerCase:
    for characters in word:
        if characters in ['!.;:,"?/=>1234567890()-']:
            word.replace(characters, '')
'''
    countWord = {}
    for word in narnya:
        if word in countWord:
            countWord[word] += 1
        else:
            countWord[word] = 1
'''

def bubbleSort(item):
    #Impliment of bubble sort, return the sorted bank of words
    '''
    :param item: list
    :param index:
    :param worldbanklist = list of unsorted tuples
    :return: list of tuples
    '''
    index = list(range(len(item)))
    for i in range(len(item)):
        for j in range(len(item)-i-1):
            if item[j] > item[j+1]:
                item[j], item[j+1] = item[j+1], item[i]
                index[j], index[j+1] = item[j+1], index[j]
    return item, index


def prebubble(wordbanklist):
    items = [element[1] for element in wordbanklist]
    items_sort, index = bubbleSort(items)
    sortwordbank = [wordbanklist[i] for i in index]
    return sortwordbank

def insertionSort(items):
    #Impliment of insertion sort, return the sorted bank of words, the faster way
    '''
    :param items:
    :return: dictionary
    '''
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
    return items

insertionSort(items=[])

i = {}
for j in lowerCase[1:100]:
    if 'x' not in i.keys():
        i[j] = lowerCase.count(j)

wordbank = printMenu(20, 20, "The Chronicles of Narnia", i)

wblist = [(k,v) for k, v in wordbank.items()]



#sortlist = prebubble(wblist[1:50])
sortlist = insertionSort(wblist[1:50])
print(wordbank)
