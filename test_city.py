import unittest
import city
import builtins

class test_City(unittest.TestCase):
    def test_Load_And_View_City(self):
        playMap = city.loadCity('start.csv')
        print_values = []
        builtins.print = lambda s: print_values.append(s)
        city.viewCity(playMap)
        assert print_values == ["    A     B     C     D   ",
                                " +-----+-----+-----+-----+",
                                "1|     |     |     |     |",
                                " +-----+-----+-----+-----+",
                                "2|     |     |     |     |",
                                " +-----+-----+-----+-----+",
                                "3|     |     |     |     |",
                                " +-----+-----+-----+-----+",
                                "4|     |     |     |     |",
                                " +-----+-----+-----+-----+",
                                '']
    def test_View_City_With_Invalid_FIle(self):
        self.assertFalse(city.loadCity('fake.txt'))