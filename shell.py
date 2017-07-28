import core, disk

def make_message():
    """ [[str, str, float, float]] -> str """
    print('Welcome to California Rentals.')
    msg = 'How many bedrooms are you looking for in a home?'
    return msg

def if_price_is_right(selection):
    ''' string -> int '''
    right = disk.price(selection)
    msg = (input('Our',right[0],'houses are', right[1], 'for monthly rent. Is this finicially possible for you?\n'))
    return msg 

def decision():
    if decision == 'no':
        print('Thank you for thinking of California Rentals during your journey of finding a home. Best of luck to you.')
    elif decision == 'yes':
        print('Wonderful. Lets talk over the taxes and additional information.')




def main():
    selection  = make_message()
    yes_no = if_price_is_right(selection)
    statement = decision()
    inv = disk.make_inventory()
    monthly = core.get_monthly_rent(inv)
    replace = core.replacement_value(inv)
    deposit = core.deposit(replace)

    






if __name__ == '__main__':
    main()
    









