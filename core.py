def make_message(inventory):
    """ string, float -> string """
    msg = 'Welcome to California Rental Homes. Beautiful area and even better homes.\n'
    for item in inventory:
        msg += '\t{}. {} ${:.2f}\n'.format(item[0], item[1], item[3])
        #found in gas core 


def total_cost(rent, amount):
    '''(string, int) -> (float)
    '''
    one_bedroom = 1000
    two_bedroom = 2000
    three_bedroom = 3000
    four_bedroom = 4000
    five_bedroom = 5000



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







 
    







