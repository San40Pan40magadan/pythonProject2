from payment import calculate as cal

def test(a, b):
    c = cal(a, b)

    assert  c > 0


test(10, 20)
test(1, 15)
test(40, 150)