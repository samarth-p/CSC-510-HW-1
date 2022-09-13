from .cols import Cols
from .csv import csv
from .row import Row


class Data:
    def __init__(self, src):
        self.cols = None
        self.rows = []
        if type(src) == str:
            csv(src, self.add)
        else:
            for row in src:
                self.add(row)
    
    def add(self, xs):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row = xs if (hasattr(xs, 'cells')) else Row(xs)
            for cols in (self.cols.x, self.cols.y):
                for col in cols:
                    col.add(row.cells[col.at]) 

    def stats(self, places, showCols, fun=None):
        t={}
        showCols = showCols or self.cols.y
        for col in showCols:
            v = (fun(col) if fun != None else col.mid())()
            v = round(v, places) if isinstance(v, float) else v
            t[col.name] = v
        return t
