'''
Created on Jul 20, 2017

@author: ahmed
'''
import re

def strongPass(password):
    lengthR = re.compile(r"\S{8,}")
    capsR = re.compile(r"[A-Z][a-z]|[a-z][A-Z]")
    digitR = re.compile(r"\d")
    lengthCheck = lengthR.search(password)
    capsCheck = capsR.search(password)
    digitCheck = digitR.search(password)

    if lengthCheck != None and capsCheck != None and digitCheck != None:
        print("Your password is very strong!")
    else:
        print("Your password is not strong enough")

strongPass(input("Please input your password to check its strength:\n"))
