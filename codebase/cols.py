import re

from codebase.num import Num
from codebase.sym import Sym


class Cols:

    def __init__(self, names) -> None:
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []

        for c, s in enumerate(self.names):
            if re.match("^[A-Z]+", s):
                col = Num(c, s)
            else:
                col = Sym(c, s)
            self.all.append(col)
            if re.search(":$", s) is None:
                if re.search("[!+-]", s):
                    self.y.append(col)
                else:
                    self.x.append(col)
                if re.search("!$", s):
                    self.klass = col
