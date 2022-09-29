import unittest
import main


class TestCase(unittest.TestCase):

    def test1(self):
        expected = True
        self.assertTrue(main.func(), expected)
