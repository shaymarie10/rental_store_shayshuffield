


def deposit(prices):
    '''(inventory, item) -> (float) 
    the variable 3 is associated in inventory as the cost of replacement. The deposit is 10% of replacement value.
    '''
    amount = prices[3] * .10
    return amount


def sales_tax(prices):
    '''(inventory, item) -> (float)
    >>>  sales_tax(1000)
    70
     '''
    amount = prices[1] * .07
    return amount




def cost(prices):
    '''List -> Float

    Returns the total cost of an item with the provided replacement value.

    >>> cost [2000]
    4000
    >>> cost [4000]
    16000
    '''
    amount = prices[1] * 4
    return amount


def take_away(selection, inventory):
    str_l = ['bedrooms, monthly_rent, quantity, cost']
    for item in inventory:
        if item[0] == selection:
            item[2] == int(item[0]) - int(item[2])
        str_l.append('{}, {}, {}, {}'.format(str(item[0]), str(item[1]), str(item[2]), str(item[3])))
        msg = '\n'.join(str_l)
    return msg


def rental_return():
    str_l = ['bedrooms, monthly_rent, quantity, cost']
    for item in inventory:
        if item[0] == decision:
            item[2] = int(item[2]) + quantity
        str_l.append('{}, {}, {}, {}'.format(str(item[0]), str(item[1]), str(item[2]), str(item[3])))
        inventory = '\n'.join(str_l)
    return inventory 
        























 
    







