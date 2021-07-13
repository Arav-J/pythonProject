import unittest


class TestCaseDemo(unittest.TestCase):

    def setUp(self):
        print('setUp method execution...')

    def test_method1(self):
        print('test method1 execution...')
        print(10/0)

    def test_method2(self):
        print('test method2 execution...')

    def tearDown(self):
        print('tearDown method execution...')

    @classmethod
    def setUpClass(cls):
        print('setUpClass method execution')


unittest.main()



