import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        expected = True
        self.assertTrue(expected, "Success")
