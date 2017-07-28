

def get_monthly_rent(rent):
    '''(string, int) -> (float)
    '''
    cash = []
    for item in rent:
        cash.append(item[1])
    return cash

def replacement_value(inv):
    '''(Item) -> (float)'''
    for item in inv:
        return item[1] * 10


def deposit(replace):
    '''(int) -> (float) '''
    return replace * .10


def sales_tax(rent, amount):
    '''(inventory, item) -> (float) '''
    for item in rent:
        amount = item[1] * .07









 
    







