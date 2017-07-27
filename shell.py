import core, disk

def main():
    selection  = core.make_message()
    rent = disk.make_inventory()
    monthly = core.get_monthly_rent(rent)
    rent = core.replacement_value(rent)
    replace = core.deposit(rent)

    rent = ''
    total_amount = 0
    while rent != 'Q'.upper():
        rent = input(selection)
        if rent == '1':
            amount = (input('\nOur one bedroom houses are 1000 for monthly rent. Is this finicially possible for you?\n'))
            if amount == 'yes':
                total_amount += core.total_cost(rent, amount)
                print('You have purchased', amount, 'house. Your total will be $' + str(core.total_cost(rent, amount)))
            elif amount == 'no':
                print('Thank you for thinking of California Rentals during your journey of finding a home. Best of luck to you.')
        if rent == '2':
            amount = (input('\nOur two bedroom houses are 2000 for monthly rent. Is this finicially possible for you?\n'))
            if amount == 'yes':
                total_amount += core.total_cost(rent, amount)
                print('You have purchased', amount, 'house. Your total will be $' + str(core.total_cost(rent, amount)))
            elif amount == 'no':
                print('Thank you for thinking of California Rentals during your journey of finding a home. Best of luck to you.')
        if rent == '3':
            amount = (input('\nOur three bedroom houses are 3000 for monthly rent. Is this finicially possible for you?\n'))
            if amount == 'yes':
                total_amount += core.total_cost(rent, amount)
                print('You have purchased', amount, 'house. Your total will be $' + str(core.total_cost(rent, amount)))
            elif amount == 'no':
                print('Thank you for thinking of California Rentals during your journey of finding a home. Best of luck to you.')
        if rent == '4':
            amount = (input('\nOur four bedroom houses are 4000 for monthly rent. Is this finicially possible for you?\n'))
            if amount == 'yes':
                total_amount += core.total_cost(rent, amount)
                print('You have purchased', amount, 'house. Your total will be $' + str(core.total_cost(rent, amount)))
            elif amount == 'no':
                print('Thank you for thinking of California Rentals during your journey of finding a home. Best of luck to you.')
        if rent == '5':
            amount = (input('\nOur five bedroom houses are 5000 for monthly rent.Is this finicially possible for you?\n'))
            if amount == 'yes':
                total_amount += core.total_cost(rent, amount)
                print('You have purchased', amount, 'house. Your total will be $' + str(core.total_cost(rent, amount)))
            elif amount == 'no':
                print('Thank you for thinking of California Rentals during your journey of finding a home. Best of luck to you.')
         




if __name__ == '__main__':
    main()
    









