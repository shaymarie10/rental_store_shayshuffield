import core



    

def test_cost():
    assert core.cost(1000) == 4000


def test_deposit():
    assert core.deposit(4000) == 400


def test_sales_tax():
    assert core.sales_tax(1000) == 70



