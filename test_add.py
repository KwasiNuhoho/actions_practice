from add import add
def test_adds_positive():
    assert add(2, 3) == 5

def test_adds_negative():
    assert add(-1, -1) == -2