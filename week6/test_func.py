from demo_func import add, multiply

# test case: second number is zero
def test_add_01():
    a = 4
    b = 0
    c = add(a, b)
    assert c == 4

# test case: both numbers are zero
def test_add_02():
    a = 0
    b = 0
    c = add(a, b)
    assert c == 0

def test_add_03():
    a = 0
    b = 4
    c = add(a, b)
    assert c == 4

def test_multply_01():
    n = 4
    p = multiply(n)
    assert p == 24

def test_multply_02():
    n = 1
    p = multiply(n)
    assert p == 1

def test_multply_03():
    n = 0
    p = multiply(n)
    assert p == 1

def test_multply_04():
    n = -1
    try:
        p = multiply(n)
        assert False
    except ValueError as e:
        assert str(e) == 'No factorial for negative number'