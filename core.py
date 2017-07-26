def make_message(inventory):
    """ string, float -> string """
    msg = 'Welcome to California Rental Homes. Beautiful area and even better homes.\n'
    for item in inventory:
        msg += '\t{}. {} ${:.2f}\n'.format(item[0], item[1], item[3])
        #found in gas core 


def monthly_rent(amount):
    '''(string, int) -> (float) '''
    one bedroom = 1000
    two bedroom = 2000
    three bedroom = 3000
    four bedroom = 4000
    five bedroom = 5000




