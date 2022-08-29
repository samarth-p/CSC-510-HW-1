import sys
sys.path.insert(0, '../code')

from area import area_of_square

def testarea():
    side = 5
    assert area_of_square(side) == 25