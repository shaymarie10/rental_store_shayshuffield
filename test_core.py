import core

def test_make_message():
    inventory = [
        ['one bedroom', 1000],
        ['two bedroom', 2000 ],
        ['three bedroom', 3000],
        ['four bedroom', 4000],
        ['five bedroom', 5000],
        ]
    expected = '''How many bedrooms are you looking for in a home?'''
    assert core.make_message() == expected

def test_get_monthly_rent():
    inventory = [
         ['one bedroom', 1000],
        ['two bedroom', 2000 ],
        ['three bedroom', 3000],
        ['four bedroom', 4000],
        ['five bedroom', 5000],
        ]
    expected = [1000, 2000, 3000, 4000, 5000]
    
    assert core.get_monthly_rent(inventory) == expected
    

def test_replacement_value():
    inventory = [
        ['one bedroom', 1000],
        ['two bedroom', 2000 ],
        ['three bedroom', 3000],
        ['four bedroom', 4000],
        ['five bedroom', 5000],
        ]
    expected = [
        ['one bedroom', 10000],
        ['two bedroom', 20000 ],
        ['three bedroom', 30000],
        ['four bedroom', 40000],
        ['five bedroom', 50000],
        ]
    assert core.replacement_value(inventory) == expected 

def test_deposit():
    inventory = [
        [replacement_value]
        ]
    expected = inventory * .10
    
    assert core.deposit(inventory) == expected 



