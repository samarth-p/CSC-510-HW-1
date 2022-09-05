import re
import sys
import random
import math


class the:
    nums = 32


class library_functions:

    def per(t, p):
        p = math.floor(((p or 0.5) * len(t)) + 0.5)

        return t[max(1, min(len(t), p)) - 1]


class Num:

    def __init__(self, c, s) -> None:
        self.n = 0
        self.at = c or 0
        self.s = s or ""
        self.has = []
        self.lo = sys.maxsize * 2 + 1
        self.hi = - sys.maxsize * 2 + 1
        self.is_sorted = True
        self.w = -1 if re.search("-$", self.s) else 1

    def nums(self):

        if not self.is_sorted:
            self.has = sorted(self.has)
            self.is_sorted = True

        return self.has

    def add(self, v):

        pos = None

        if v != "?":
            self.n += 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)

            if len(self.has) < the.nums:
                self.has.append(v)
                self.is_sorted = False

            elif random.random() < the.nums / self.n:
                pos = random.randint(0, len(self.has) - 1)
                self.has[pos] = v
                self.is_sorted = False

    def div(self):
        a = self.nums()
        return (library_functions.per(a, 0.9) - library_functions.per(a, 0.1)) / 2.58

    def mid(self):

        return library_functions.per(self.nums(), 0.5)
