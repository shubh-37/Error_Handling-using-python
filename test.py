'''
This is test file that uses Unit testing to check for errors in our methods and functions
'''
import unittest
import mainfile

class TestCap(unittest.TestCase):

    def test_cap_first(self):
        test = 'shubh in cu'
        result = mainfile.cap_first(test)
        self.assertEqual(result,'Shubh in cu')

    def test_cap_all(self):
        test = 'shubh in cu'
        result = mainfile.cap_all(test)
        self.assertEqual(result,'Shubh In Cu')

if __name__ == '__main__':
    unittest.main()