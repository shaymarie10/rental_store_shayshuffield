import core, disk

def make_message():
    """ [[str, str, float, float]] -> str """
    print('Welcome to California Rentals.')
    msg = input('How many bedrooms are you looking for in a home?')
    return msg

def if_price_is_right(selection):
    ''' string -> int '''
    right = disk.price(selection)
    msg = input('Our '+ str(right[0])+' houses are '+ str(right[1])+ ' for monthly rent. Is this finicially possible for you?')
    return msg 

def decision(yes_no, selection, sale_tax, dollars):
    if yes_no == 'no':
        print('Thank you for thinking of California Rentals during your journey of finding a home. Best of luck to you.')
    elif yes_no == 'yes':
        input('The total sales tax for a ' + str(selection) + ' bedroom house is ' + str(sale_tax) + ' dollars. Push enter to continue ')
        print('Please take note that we have a replacement policy. Our ' + str(selection) + ' bedroom houses are ' + str(dollars) + ' if destruction occurs. ')
        




def main():
    selection  = make_message() 
    yes_no = if_price_is_right(selection)
    prices = disk.price(selection)
    sale_tax = core.sales_tax(prices)
    deposit = core.deposit(prices)
    dollars = core.cost(deposit)
    statement = decision(yes_no, selection, sale_tax, dollars)

    






if __name__ == '__main__':
    main()
    









