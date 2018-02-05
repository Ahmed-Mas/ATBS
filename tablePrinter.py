'''
Created on Jul 20, 2017

@author: ahmed
prints a list of strings in table format
'''
from builtins import len

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)
    z = 0
    for li in table:
        for item in li:
            if len(item) > colWidths[z]:
                colWidths[z] = len(item)
        z += 1
    print(colWidths)
    z = 0
    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(colWidths[z]), end=" ")
            z += 1
        print("\n")
        z = 0

printTable(tableData)
