class Row:
    def __init__(self, t) :
        self.cells = t
        self.isEvaled = False
        self.cooked = t.copy()