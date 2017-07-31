import core



    

def test_cost():
    assert core.cost(1000) == 10000


def test_deposit():
    assert core.deposit(1000) == 100

def test_sales_tax():
    assert core.sales_tax(1000) == 70



