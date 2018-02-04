import re, os, shutil

reg = re.compile(r".+\.txt")

sendingItems = []

def moveNew(curPath):
    for x in os.listdir(curPath):
        hits = reg.search(x)
        if hits != None:
            sendingItems.append(curPath + "\\" + hits.group())

        elif os.path.isdir(curPath + "\\" + x):
            moveNew(curPath + "\\" + x)

    for txtFile in sendingItems:
        shutil.copy(txtFile, "C:\\Users\\ahmed\\Desktop\\newFolder")

moveNew("C:\\Users\\ahmed\\Desktop\\test")
