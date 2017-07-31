


def deposit(prices):
    '''(inventory, item) -> (float) '''
    amount = prices[1] * .10
    return amount


def sales_tax(prices):
    '''(inventory, item) -> (float) '''
    amount = prices[1] * .07
    return amount

def cost(deposit: float) -> float:
    '''Float -> Float

    Returns the total cost of an item with the provided replacement value.

    >>> cost(100)
    1000
    >>> cost(1000)
    10000
    '''
    return int(deposit) * 10











 
    







