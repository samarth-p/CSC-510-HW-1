import inspect
import random
import sys
import traceback

from codebase.cli import the
from codebase.csv import csv
from codebase.data import Data
from codebase.num import Num
from codebase.sym import Sym

n = 0


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
    
    def test_data(self):
        data = Data(the['file'])

        for col in data.cols.y:
            print(col)

        return True

    def test_stats(self):
        data = Data(the['file'])
        div = lambda col: col.div
        mid = lambda col: col.mid

        print("xmid", f"{data.stats(2, data.cols.x, mid)}")
        print("xdiv", f"{data.stats(3, data.cols.x, div)}")
        print("ymid", f"{data.stats(2, data.cols.y, mid)}")
        print("ydiv", f"{data.stats(3, data.cols.y, div)}")

        return True

    def test_csv(self):

        def fun(row):
            global n
            n = n + 1
            if n > 10:
                return
            else:
                print(row)
        csv(the['file'], fun)

        return True


def runs(test_name):
    tests_obj = Tests()
    list_of_tests = dict(inspect.getmembers(tests_obj, predicate=inspect.ismethod))

    # Set the random seed from command-line
    random.seed(the['seed'])

    if test_name.lower() == "all":
        tests_to_run = list_of_tests
    elif test_name in list_of_tests.keys():
        tests_to_run = dict([(test_name, list_of_tests.get(test_name))])
    else:
        print("Test '{}' not found".format(test_name))
        return

    passed_test = 0

    # Save the initial values saved in 'the'
    initial_the = the.copy()

    for test_num, (test_name, test_function) in enumerate(tests_to_run.items(), start=1):

        print("")
        print("------------------------------")
        print("Running Test #{} - {}".format(test_num, test_name))
        print("------------------------------")

        status = False

        # Call the test function
        try:
            out = test_function()
            status = True

        except Exception as e:
            out = e
            if the['dump']:
                print(traceback.format_exc())
                sys.exit(1)

        if out is True:
            passed_test += 1

        msg = status and ((out is True and "PASS") or "FAIL") or "CRASH"

        print("------------------------------")
        print("{} - Test #{} - {}".format(msg, test_num, test_name))
        print("------------------------------")

        # Restore initial value for 'the'
        for k, _ in the.items():
            the[k] = initial_the[k]

    print("")
    print("------------------------------")
    print("Test Summary - {}/{} PASSED".format(passed_test, len(tests_to_run)))
    print("------------------------------")


# Run the test engine
runs(the['eg'])
