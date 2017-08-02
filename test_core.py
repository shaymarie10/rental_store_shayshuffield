import core

def test_cost():
    inventory = [ 'a',1000,'c','d']
    assert core.cost(inventory) == 4000


def test_deposit():
    inventory = ['a', 'b', 'c', 4000]
    assert core.deposit(inventory) == 400


def test_sales_tax():
    inventory = ['a', 1000, 'c', 'd']
    assert core.sales_tax(inventory) == 70

def test_take_away():
    inventory = [
        ['1', 1000.0, 100.0, 4000.0],
    ]
    assert core.take_away('1', inventory) == ['1', 1000.0, 99.0, 4000.0]
    
