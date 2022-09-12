import inspect
import random
import sys
import traceback

from codebase.cli import the
from codebase.num import Num
from codebase.sym import Sym


class Tests:

    def test_num(self):

        num = Num()
        the['nums'] = 100

        for i in range(1, 101):
            num.add(i)

        mid, div = num.mid(), num.div()
        print("List of numbers : {}".format(num.nums()))
        print("Median : {}".format(mid))
        print("Standard deviation : {}".format(div))
        return 50 <= mid <= 52 and 30.5 < div < 32

    def test_bignum(self):
        num = Num()
        the['nums'] = 32

        for i in range(1, 1001):
            num.add(i)

        print("List of numbers : {}".format(num.nums()))
        return 32 == len(num.has)

    def test_sym(self):
        sym = Sym()
        sample_list = ["a", "a", "a", "a", "b", "b", "c"]
        for element in sample_list:
            sym.add(element)
        mode, entropy = sym.mid(), sym.div()
        entropy = (1000 * entropy) // 1 / 1000
        print("Mode : {}".format(mode))
        print("Entropy : {}".format(entropy))
        return mode == 'a' and 1.37 <= entropy <= 1.38

    def test_the(self):
        print("List of config parameters : {}".format(the))
        return True
