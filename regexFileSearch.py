import re, os

path = "C:\\Users\\ahmed\\Desktop\\test"

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