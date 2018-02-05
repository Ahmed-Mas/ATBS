'''
Created on Jul 20, 2017

@author: ahmed
runs through all .txt files in directory to look for word
'''
import re, os

path = input("Please input full location..\n")

os.chdir(path)

userI = input("Please input regex pattern:\n")
userR = re.compile(userI)

for file in os.listdir(path):
    if ".txt" in file:
        curF = open(file, "r")
        docT = curF.read()
        hits = userR.search(docT)
        if hits != None:
            print(file + ":\n" + hits.group() + "\n\n")