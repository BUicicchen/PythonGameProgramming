'''This program is a dictionary between French and English, translate the English numbers to French, vice versa'''

# Add the number up to ten to the dictionary
english2french = {'one':'un','two':'deux','three':'trois','four':'quatre','five':'cinq','six':'six','seven':'sept','eight':'huit','nine':'neuf', 'ten':'dix'}
# how can we get the first element in the dictionary?
# the answer is no we can't get the first element in dicitonary because there are no position in dictionary

for k, v in english2french.items():
        print(k, str(v))

for v in english2french.values():
        print(v)

for v in english2french.keys():
        print(v)

print english2french.get('two')

deleteElement = english2french['one']
print(deleteElement)

copyOfDic = english2french.copy()
print(copyOfDic)

copyFromKeys = english2french.fromkeys('one')
print(copyOfDic)

userNumber = raw_input("Please enter a number you want to translate: ")
print(type(userNumber))
if userNumber in english2french:
    print('Yes')
else:
    print('No')

clearDic = english2french.clear()
print(clearDic)
