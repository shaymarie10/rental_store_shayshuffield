def make_message():
    """ [[str, str, float, float]] -> str """
    print('Welcome to California Rentals.')
    msg = 'How many bedrooms are you looking for in a home?'
    return msg

def get_monthly_rent(rent):
    '''(string, int) -> (float)
    '''
    cash = []
    for item in rent:
        cash.append(item[1])
    return cash

def replacement_value(rent):
    '''(int, float) -> (float)'''
    for item in rent:
        rent = item[1] * 10
    return rent 


def deposit(replacement):
    '''(list, int) -> (int) '''
    


    








def deposit(replacement):
    '''(List, int) -> (int)
    '''
    amount = [
        ['one_bedroom', 1000],
        ['two_bedroom', 2000],
        ['three_bedroom', 3000],
        ['four_bedroom', 4000],
        ['five_bedroom', 5000]
    ]
    replacement = amount 
    replacement * .10 == deposit 


def sales_tax(tax):
    '''(List, float) -> (float)'''





#Sales Tax
    if rent == '1':
        return float(round(one_bedroom * amount, 2))
    if rent == '2':
        return float(round(two_bedroom * amount, 2))
    if rent == '3':
        return float(round(three_bedroom * amount, 2))
    if rent == '4':
        return float(round(four_bedroom* amount, 2))
    if rent == '5':
        return float(round(five_bedroom * amount, 2))







 
    







