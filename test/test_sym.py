from codebase.sym import Sym
from codebase.cli import the


def test_sym():
    sym = Sym()
    sample_list = ["a", "a", "a", "a", "b", "b", "c"]
    for element in sample_list:
        sym.add(element)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000*entropy)//1/1000
    print("Mode : {}" .format(mode))
    print("Entropy : {}" .format(entropy))
    assert mode == 'a' and 1.37 <= entropy <= 1.38


def test_the():
    print("List of config parameters : {}" .format(the))
    assert True
