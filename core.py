

def get_monthly_rent(rent):
    '''(string, int) -> (float)
    '''
    cash = []
    for item in rent:
        cash.append(item[1])
    return cash


def deposit(replace):
    '''(int) -> (float) '''
    return replace * .10


def sales_tax(rent, amount):
    '''(inventory, item) -> (float) '''
    for item in rent:
        amount = item[1] * .07

def cost(replace: float) -> float:
    '''Float -> Float

    Returns the total cost of an item with the provided replacement value.

    >>> cost(100)
    1000
    >>> cost(1000)
    10000
    '''
    return replace * 10









 
    







