import numpy as np
import unittest


class QuestionTest1(unittest.TestCase):
    
    def __init__(self, fair_dice):
        self.func = fair_dice

    def test_support(self):
        for i in range(1, 7):
            self.assertAlmostEqual(self.func(i), 1/6)

    def test_not_support(self):
        self.assertAlmostEqual(self.func(-1), 0)
        self.assertAlmostEqual(self.func(10), 0)
        self.assertAlmostEqual(self.func(3.4), 0)
        self.assertAlmostEqual(self.func(900), 0)
        self.assertAlmostEqual(self.func(np.exp(1)), 0)
       
    def run(self):
        self.test_support()
        self.test_not_support()
        print("All tests are passed")