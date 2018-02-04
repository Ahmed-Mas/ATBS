'''
Created on Jul 20, 2017

@author: ahmed
'''

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    itemsTotal = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        itemsTotal += v
    print("Total Items: " + str(itemsTotal))

displayInventory(stuff)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    displayInventory(inventory)

addToInventory(stuff, dragonLoot)