import unittest
import foo
class TestFoo(unittest.TestCase):
    def test_add_two_int(self):
        result = foo.add_int(1,2)
        self.aseertEquals(result, 3)