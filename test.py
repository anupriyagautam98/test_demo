import unittest

class Test(unittest.TestCase):
    def test(self):
        a=15
        self.assertEqual(a,15)

if __name__=='__main__':
    unittest.main()