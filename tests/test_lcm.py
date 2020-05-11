import unittest
from algorithms.lcm import lcm

class TestLcm(unittest.TestCase):

    def test_true_case1(self):
        self.assertEqual(lcm(124, 241), 29884)

    def test_true_case1(self):
        self.assertEqual(lcm(428, 631), 270068)