import core

def make_message():
    inventory = [
        ['one bedroom', 1000],
        ['two bedroom', 2000 ],
        ['three bedroom', 3000],
        ['four bedroom', 4000],
        ['five bedroom', 5000],
        ]
    expected = '''Welcome to California Rental Homes. We have several homes to choose from.
\t1. one bedroom
\t2. two bedroom
\t3. three bedroom
\t4. four bedroom
\t5. five bedroom
'''
    assert core.make_message(inventory) == expected
    

