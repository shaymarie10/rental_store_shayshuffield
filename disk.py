import core


def make_inventory():
    left = []
    with open('inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([
            split_string[0],
            float(split_string[1]),
            float(split_string[2]),
            float(split_string[3])
        ])
    return left


def item(num_of_beds):
    prices = make_inventory()
    for item in prices:
        if item[0].startswith(num_of_beds):
            return item


def change_inventory(select):
    with open('inventory.txt', 'w') as file:
        file.write(select)
    return True


def get_log(num_of_beds, quantity, total, prices):
    msg = '{}, {}, {}\n'.format(num_of_beds, quantity, total, prices)
    with open('history.txt', 'a') as file:
        file.write(msg)


def revenue():
    left = []
    with open('history.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
        for line in lines:
            split_string = line.strip().split(', ')
            left.append(float(split_string[2]))
        return sum(left)
