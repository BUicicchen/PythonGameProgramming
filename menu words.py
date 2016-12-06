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
narnya = glossary[start:finish]
print(narnya)



lwidth = 20
rwidth = 20
title = "The Chronicles of Narnia"
def printMenu(lwidth, rwidth, title):
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

    countWord = {}
    for word in glossary:
        if word in countWord:
            countWord[word] += 1
        else:
            countWord[word] = 1
    for k, v in countWord.items():
        print(k.ljust(lwidth, ".") + str(v).rjust(rwidth, "."))

menu = printMenu(lwidth, rwidth, title)
