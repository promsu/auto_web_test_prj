import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner


class WebTest(unittest.TestCase):

    def setUp(self):
        print('test start ...')

    def test_title(self):
        print('test_title running ...')

    def test_001(self):
        print('test_001 running ...')

    def test_002(self):
        self.assertEqual(1, 2, '1 = 2')
        print('test_002 running ...')

    def tearDown(self):
        print('test ending ...')


if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(WebTest('test_001'))
    suit.addTest(WebTest('test_002'))
    runner = unittest.TextTestRunner()
    runner.run(suit)
