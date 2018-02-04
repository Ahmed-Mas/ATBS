'''
Created on Jul 20, 2017

@author: ahmed
'''

def addWord():
    spam = []
    while (input("Would you like to add a word? Y/N\n") == "Y"):
        spam.append(input("What word would you like to add?\n"))
    return spam

def commaCode(someList):
    print("Your list of words with commas:\n")
    phrase = ""
    for x in range(len(someList)):
        if x < len(someList) - 2:
            phrase += someList[x] + ", "
        elif x == len(someList) - 2:
            phrase += someList[x] + ", and "
        else:
            phrase += someList[x]
    print(phrase)

commaCode(addWord())
