from super_duper_add import add


def test_add_simple():
    assert add(2, 3) == 5


def test_add_negs():
    assert add(-1, -2) == -3


def test_add_neg_pos():
    assert add(1, -1) == 0


def test_add_zero():
    assert add(1, 0) == 1


def test_add_zeros():
    assert add(0, 0) == 0
