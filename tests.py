import unittest
from backend import main


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "I made it to the other file."
        self.assertTrue(main.test_function(), expected)
