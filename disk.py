import core

def make_inventory():
    left = []
    with open('inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], float(split_string[1]), float(split_string[2])])
    return left

def price(selection):
    price = make_inventory()
    for item in price:
        if item[0].startswith(selection):
            return item


    