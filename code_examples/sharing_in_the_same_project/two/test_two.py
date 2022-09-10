def test_cube(blue):
    x = 7
    y = pow(x, 3)
    expected = x * x * x
    blue(f'{x=}, {y=}, {expected=}')
    assert y == expected