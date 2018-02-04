'''
Created on Jul 20, 2017

@author: ahmed
'''
spam = ["apples", "bananas", "tofu", "cats"]

def commaCode(someList):
    phrase = ""
    for x in range(len(someList)):
        if x < len(someList) - 2:
            phrase += someList[x] + ", "
        elif x == len(someList) - 2:
            phrase += someList[x] + ", and "
        else:
            phrase += someList[x]
    print(phrase)

commaCode(spam)