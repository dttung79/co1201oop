from product import Product

def test_product_init():
    p = Product('apple', 10, 5)
    assert p.name == 'apple'
    assert p.price == 10
    assert p.quantity == 5

def test_product_name_setter_01():
    p = Product('apple', 10, 5)
    p.name = 'banana'
    assert p.name == 'banana'

def test_product_price_setter_01():
    p = Product('apple', 10, 5)
    p.price = 20
    assert p.price == 20

def test_product_quantity_setter_01():
    p = Product('apple', 10, 5)
    p.quantity = 10
    assert p.quantity == 10

def test_product_name_setter_02():
    p = Product('apple', 10, 5)
    try:
        p.name = ''
        assert False
    except ValueError as e:
        assert str(e) == 'Name cannot be empty'

def test_product_price_setter_02():
    p = Product('apple', 10, 5)
    try:
        p.price = -1
        assert False
    except ValueError as e:
        assert str(e) == 'Price cannot be negative'

def test_product_quantity_setter_02():
    p = Product('apple', 10, 5)
    try:
        p.quantity = -1
        assert False
    except ValueError as e:
        assert str(e) == 'Quantity cannot be negative'


def test_product_show(capsys):
    p = Product('apple', 10, 5)
    p.show()
    captured = capsys.readouterr()
    assert captured.out == 'Name: apple, price: $10, quantity: 5\n'