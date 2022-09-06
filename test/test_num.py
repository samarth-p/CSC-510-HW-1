from codebase.num import Num
from codebase.cli import the


def test_num():
    num = Num()

    for i in range(1, 101):
        num.add(i)

    mid, div = num.mid(), num.div()
    print("List of numbers : {}" .format(num.nums()))
    print("Median : {}" .format(mid))
    print("Standard deviation : {}" .format(div))
    assert 50 <= mid <= 52 and 30.5 < div < 32


def test_bignum():
    num = Num()
    the['nums'] = 32

    for i in range(1, 1001):
        num.add(i)

    print("List of numbers : {}" .format(num.nums()))
    assert 32 == len(num.has)
