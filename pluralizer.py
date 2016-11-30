'''This program changes nouns in singular form into plural form if the quantity is more than one within 1~10'''


#asks the user of the noun to be pluralized
word = raw_input("Please enter a noun to be pluralized: ")

#asks the user for the number of objects
number = input("Please enter the number of the noun: ")

#dictionary for the pluralizer
pluralizer = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}
#dictionary for the exceptions
exceptions = {'mouse':'mice', 'person':'people', 'deer':'deer', 'potato':'potatoes', 'man':'men', 'child':'children'}

def numberObjects(number):
    #this function checks whether the input number is valid
    '''
    :param number: quantity of the noun, has to be between 1 and 10
    :return: None
    '''
    if number < 1 and number > 10:
        print("Invalid number!")
        number = int(input("Please enter the number of the noun again (1~10): "))

def pluralForm(word, number):
    #this function prints the plural form of the noun inputted
    '''
    :param word: word entered to be pluralized
    :param number: quantity of the noun, has to be between 1 and 10
    :return: word, plural
    '''

    if number == 1:
        return word
    elif number in range (2,10):
        if word in exceptions.keys():
            plural = exceptions[word]
        elif word[-2:] == "ch" or word[-2:] == "sh" or word[-1:] == "s" or word[-1:] == "x" or word[-1:] == "z":
            plural = word + "es"
        elif word[-1:] == "y" and word[-2:] != "ay" and word[-2:] != "ey" and word[-2:] != "iy" and word[-2:] != "oy" and word[-2:] != "uy":
            plural = word.replace("y", "ies")
        elif word[-1:] == "f":
            plural = word.replace("f", "ves")
        elif "oo" in word:
            plural = word.replace("oo", "ee")
        else:
            plural = word + "s"
        return plural

numberObjects(number)
plural = pluralForm(word, number)
print(pluralizer[number] + " " + plural)
