def make_message():
    """ [[str, str, float, float]] -> str """
    msg = 'Welcome to California Rentals. How many bedrooms are you looking for in a home?\n'
    return msg

def get_monthly_rent(rent):
    '''(string, int) -> (float)
    '''
    cash = []
    for item in rent:
        cash.append(item[1])
    return cash

def replacement_value(rent):
    '''int, float) -> (float)'''
    for item in rent:
        rent = item[1] * 10
    return rent








def refill():
    str_l = ['type, amount_in_tank, price']
    left = in_the_tank()
    for item in left:
        if item[1] < 5000.0:
            item[1] = 5000.0
        item[1]=str(item[1])
        item[2]=str(item[2])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)

    with open('tank.txt', 'w') as file:
        file.write(message) 

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







 
    







