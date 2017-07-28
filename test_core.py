import core


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
    item = ['one bedroom', 1000]
    expected = 10000

    assert core.replacement_value(item) == expected 

def test_deposit():
    assert core.deposit(1000) == 100

def test_sales_tax(amount):
    assert core.sales_tax(1000) == 70



