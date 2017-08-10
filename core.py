def deposit(prices):
    '''(inventory, item) -> (float) 
    the variable 3 is associated in inventory as the cost of replacement. The deposit is 10% of replacement value.
    '''
    amount = float(prices[3]) * .10
    return amount


def sales_tax(prices):
    '''(inventory, item) -> (float)
    >>>  sales_tax(1000)
    70
     '''
    amount = float(prices[1]) * .07
    return amount


def cost(prices):
    '''List -> Float

    Returns the total cost of an item with the provided replacement value.

    >>> cost [2000]
    8000
    >>> cost [4000]
    16000
    '''
    amount = prices[1] * 4
    return amount


def take_away(num_of_beds, inventory):
    ''' str, [str] -> [inventory] '''
    for item in inventory:
        if item[0] == num_of_beds:
            item[2] = (item[2]) - 1
    return item


def rental_return(inventory, num_of_beds, quantity):
    ''' (int) -> float
    return total rented item to inventory.
    '''
    str_l = ['bedrooms, monthly_rent, quantity, cost']
    for item in inventory:
        if item[0] == num_of_beds:
            item[2] = quantity
        str_l.append(
            '{}, {}, {}, {}'.format(item[0], item[1], item[2], item[3]))
    inventory = '\n'.join(str_l)
    return inventory


def total_amount_to_user(right, prices, deposits):
    sale_tax = sales_tax(right)
    total = sale_tax + deposits + right[1]
    return total


def history(num_of_beds, quantity, total, prices):
    if num_of_beds == prices[0]:
        return prices[1]
