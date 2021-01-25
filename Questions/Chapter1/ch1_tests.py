import numpy as np
import unittest


class Question1(unittest.TestCase):
    
    def __init__(self, fair_dice):
        super().__init__()
        self.func = fair_dice

    def test_support(self):
        for i in range(1, 7):
            self.assertAlmostEqual(self.func(i), 1/6)

    def test_not_support(self):
        self.assertEqual(self.func(-1), 0)
        self.assertEqual(self.func(10), 0)
        self.assertEqual(self.func(3.4), 0)
        self.assertEqual(self.func(900), 0)
        self.assertEqual(self.func(np.exp(1)), 0)
        
    def run(self):
        self.test_support()
        self.test_not_support()
        print("All tests are passed")
        
        
class Question2(unittest.TestCase):
    
    def __init__(self, fair_dice):
        super().__init__()
        self.func = fair_dice
        
    def test_prism_k(self):
        for _ in range(100):
            N = np.random.randint(1, 1000)
            for _ in range(1, min(10, N)):
                x = np.random.randint(1, N+1)
                self.assertAlmostEqual(self.func(N, x), 1/N)
                self.assertAlmostEqual(self.func(N, x+N), 0)
                self.assertAlmostEqual(self.func(N, x-N), 0)
        
    def run(self):
        self.test_prism_k()
        print("All tests are passed")