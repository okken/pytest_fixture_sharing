def test_square(blue):
    x = 7
    y = x**2
    expected = x * x
    blue(f'{x=}, {y=}, {expected=}')
    assert y == expected

