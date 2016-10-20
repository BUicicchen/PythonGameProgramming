import myLib as ml

sampleText = 'Stand_in_the_light'
#print(ml.readTxt(sampleText))
text = ml.readTxt(sampleText)
print(type(text))


#print the following 100 words of the word searched
seedword = 'rikki-tikki'
print(seedword)
for x in range(100):
    words, freq = ml.findNextWord(seedword, text)
    prob = ml.probOccurrence(freq)
    #print(words, freq)
    #print(prob)
    newWord = ml.randomWord(words, density=prob)
    print(newWord)
    seedword = newWord

#print()
