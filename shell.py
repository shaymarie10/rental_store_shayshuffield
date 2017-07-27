import core, disk

def main():
    selection  = core.make_message()
    rent = disk.make_inventory()
    monthly = core.get_monthly_rent(rent)
    rent = core.replacement_value(rent)

    rent = ''
    total_amount = 0
    while rent != 'Q'.upper():
        rent = input(selection)
        if rent == '1':
            amount = int(input('\nOur one bedroom houses are 1000 for monthly rent. Is this a finicially possible for you?\n'))
            total_amount += core.total_cost(rent, amount *.07)
            print('You have purchased', amount, 'house. Your total will be $' + str(core.total_cost(rent, amount)))
        if rent == '2':
            amount = int(input('\nOur two bedroom houses are 2000 for monthly rent. Deposits are half the cost of the rent\n'))
            total_amount += core.total_cost(rent, amount *.07)
            print('You have purchased', amount, 'house. Your total will be $' + str(core.total_cost(rent, amount)))
        if rent == '3':
            amount = int(input('\nOur three bedroom houses are 3000 for monthly rent. Deposits are half the cost of the rent\n'))
            total_amount += core.total_cost(rent, amount *.07)
            print('You have purchased', amount, 'house. Your total will be $' + str(core.total_cost(rent, amount)))
        if rent == '4':
            amount = int(input('\nOur four bedroom houses are 4000 for monthly rent. Deposits are half the cost of the rent\n'))
            total_amount += core.total_cost(rent, amount *.07)
            print('You have purchased', amount, 'house. Your total will be $' + str(core.total_cost(rent, amount)))
        if rent == '5':
            amount = int(input('\nOur five bedroom houses are 5000 for monthly rent. Deposits are half the cost of the rent\n'))
            total_amount += core.total_cost(rent, amount *.07)
            print('You have purchased', amount, 'house. Your total will be $' + str(core.total_cost(rent, amount)))
         




if __name__ == '__main__':
    main()
    









