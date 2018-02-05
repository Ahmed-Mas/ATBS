'''
Created on Jul 20, 2017

@author: ahmed
simple brute force for pdfs using dictionary
'''
import PyPDF2

pdf = PyPDF2.PdfFileReader(open(input("Please enter the full path of the file:\n"), "rb"))

passDic = open(input("Please enter full path of dictionary:\n"))

temp = passDic.read().splitlines()

dec = False

for word in temp:
    print("Checking.. " + word)
    if pdf.decrypt(word) == 1:
        print("Password is..\n" + word)
        dec = True
        break

if dec == False:
    print("Sorry, couldn't find the password in dictionary..\n")