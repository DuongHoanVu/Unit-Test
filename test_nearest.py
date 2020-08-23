from nearest import nearest_square

def test_nearest_5():
    assert(nearest_square(5) == 4)

def test_nearest_9():
    assert(nearest_square(9) == 9)

def test_nearest_23():
    assert(nearest_square(23) == 16)