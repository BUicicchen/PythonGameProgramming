pluralize = {'chair':'', 'book':'', 'family':'', 'potato':'', 'witch':'', 'candy':'', 'woman':'', 'child':'', 'fungus':'', 'sheep':'', 'loaf':'', 'horse':'', 'deer':'', 'foot':'', 'hero':'', 'baby':''}
pluralList = []

def plurals(chairs, books, families, potatoes, witches, candies, women, children, fungi, sheep, loaves, horses, deer, feet, heroes, babies):
    pluralize["chair"] = chairs
    pluralize["book"] = books
    pluralize["family"] = families
    pluralize["potato"] = potatoes
    pluralize["witch"] = witches
    pluralize["candy"] = candies
    pluralize["woman"] = women
    pluralize["child"] = children
    pluralize["fungus"] = fungi
    pluralize["sheep"] = sheep
    pluralize["loaf"] = loaves
    pluralize["horse"] = horses
    pluralize["deer"] = deer
    pluralize["foot"] = feet
    pluralize["hero"] = heroes
    pluralize["baby"] = babies
    pluralList.append(pluralize)
    return pluralList

def displayPluralList(pluralList):
    for i in pluralList:
        print('The plural form of chair is ' + i["chair"] + '.')
        print('The plural form of book is ' + i["book"] + '.')
        print('The plural form of family is ' + i["family"] + '.')
        print('The plural form of potato is ' + i["potato"] + '.')
        print('The plural form of witch is ' + i["witch"] + '.')
        print('The plural form of candy is ' + i["candy"] + '.')
        print('The plural form of woman is ' + i["woman"] + '.')
        print('The plural form of child is ' + i["child"] + '.')
        print('The plural form of fungus is ' + i["fungus"] + '.')
        print('The plural form of sheep is ' + i["sheep"] + '.')
        print('The plural form of loaf is ' + i["loaf"] + '.')
        print('The plural form of horse is ' + i["horse"] + '.')
        print('The plural form of deer is ' + i["deer"] + '.')
        print('The plural form of foot is ' + i["foot"] + '.')
        print('The plural form of hero is ' + i["hero"] + '.')
        print('The plural form of baby is ' + i["baby"] + '.')

plural = plurals("chairs", "books", "families", "potatoes", "witches", "candies", "women", "children", "fungi", "sheep", "loaves", "horses", "deer", "feet", "heroes", "babies")
displayPluralList(pluralList)
