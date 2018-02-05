'''
Created on Jul 20, 2017

@author: ahmed
simple impossible math problem
'''
def collatz(x):
    if x % 2 == 0 and x != 1:
        print(x / 2)
        collatz(x / 2)
    elif x % 2 != 0 and x != 1:
        print(3 * x + 1)
        collatz(3 * x + 1)

try:
    collatz(int(input("Please enter a number:\n")))
except:
    print("Please enter only digits")
