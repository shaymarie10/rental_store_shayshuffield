import core, disk

def main():
    selection  = """
            Welcome to California Rental Homes. Beautiful area and even better living quarters.
What size home are you interested at looking at today?

1. one bedroom(1000)
2. two bedroom(2000)
3. three bedroom(3000)
4. four bedroom(4000)
5. five bedroom(5000)
"""


    rent = ''
    total_amount = 0
    while rent != 'Q'.upper():
        rent = input(selection)
        if rent == '1':
            amount = int(input('\nOur one bedroom houses are 1000 for monthly rent. Deposits are half the cost of the rent\n'))
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
    









