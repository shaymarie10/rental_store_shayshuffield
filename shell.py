import core, disk, time


def welcoming():
    '''str -> str '''
    print(
        '''Welcome to California Rentals. This department deals with the following.\n
    \t1. End of a lease process
    \t2. Providing information on rental homes and prices
    \t3. Revenue ''')
    time.sleep(1)


def make_message():
    """ [[str, str, float, float]] -> str """
    msg_1 = input(
        'Is your lease up with California Rentals?(if you don/t have a lease and wish to proceed with option 2 please type no)'
    )
    return msg_1


def user_gets_deposit():
    ''' string -> int '''
    selection = input(
        'We have single bedroom homes all the way up to 5 bedroom homes. What would suit you best?'
    )
    prices = disk.item(selection)
    lease = core.deposit(prices)
    print('Your return deposit will be ' + str(lease))
    return selection


def bedrooms():
    print('Lets begin the search of your perfect home')
    time.sleep(1)
    selection = input('How many bedrooms are you looking for in a home?')
    return selection


def if_price_is_right(num_of_beds):
    ''' string -> int '''
    right = disk.item(num_of_beds)
    msg = input('Our ' + str(right[0]) + ' houses are ' + str(right[1]) +
                ' for monthly rent. Is this finicially possible for you?')
    return msg


def decision(yes_no, num_of_beds, sale_tax, dollars, deposit):
    if yes_no == 'no':
        print(
            'Thank you for thinking of California Rentals during your journey of finding a home. Best of luck to you.'
        )

    if yes_no == 'yes':
        input('The total sales tax for a ' + str(num_of_beds) +
              ' bedroom house is ' + str(sale_tax) +
              ' dollars. Push enter to continue ')
        print('Our deposit for the ' + str(num_of_beds + ' bedroom houses are '
                                           + str(deposit) + ' total '))
        time.sleep(1)
        print(' Liability of ' + str(dollars) +
              ' dollars if destruction occurs. ')


def main():
    inventory = disk.make_inventory()
    left = disk.revenue()
    greet = welcoming()
    selection = make_message()
    if selection.lower() == 'revenue':
        left = disk.revenue()
        print('${:.2f}'.format(left))
    if selection.lower() == 'yes':
        num_of_beds = user_gets_deposit()
        old_quantity = disk.item(num_of_beds)[2]
        quantity = old_quantity + 1
        select = core.rental_return(inventory, num_of_beds, quantity)
        disk.change_inventory(select)
    if selection.lower() == 'no':
        num_of_beds = bedrooms()
        yes_no = if_price_is_right(num_of_beds)
        prices = disk.item(num_of_beds)
        sale_tax = core.sales_tax(prices)
        deposits = core.deposit(prices)
        dollars = core.cost(prices)
        statement = decision(yes_no, num_of_beds, sale_tax, dollars, deposits)
        inven = core.take_away(num_of_beds, inventory)
        old_quantity = disk.item(num_of_beds)[2]
        quantity = old_quantity - 1
        lease = core.rental_return(inventory, num_of_beds, quantity)
        select = core.rental_return(inventory, num_of_beds, quantity)
        disk.change_inventory(select)
        right = disk.item(num_of_beds)
        print('Your final total will be ${:.2f}'.format(
            core.total_amount_to_user(right, prices, deposits)))
        prices = disk.make_inventory()
        total = core.total_amount_to_user(right, prices, deposits)
        core.history(num_of_beds, quantity, total, prices)
        disk.get_log(num_of_beds, quantity, total, prices)


if __name__ == '__main__':
    main()
