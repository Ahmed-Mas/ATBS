'''
Created on Jul 20, 2017

@author: ahmed
copies all files from directory with user chosen extention to user chosen folder
'''
import re, os, shutil


searchFor = input("What file extention do you want to search for..\n")
copyTo = input("Where would you like to copy to..\n")
sendingItems = []
reg = re.compile(r".+\." + searchFor)

def moveNew(curPath):
    for x in os.listdir(curPath):
        hits = reg.search(x)
        if hits != None:
            sendingItems.append(curPath + "\\" + hits.group())

        elif os.path.isdir(curPath + "\\" + x):
            moveNew(curPath + "\\" + x)

    for txtFile in sendingItems:
        if ((os.path.exists(copyTo)) == False):
            os.makedirs(copyTo)
            shutil.copy(txtFile, copyTo)
        else:
            shutil.copy(txtFile, copyTo)


moveNew(input("Where would you like to copy from..\n"))
