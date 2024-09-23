import unittest
from ..is_palindrome import IsPalindrome

class TestIsPalindrome(unittest.TestCase):

    def test_sol1(self):
        test_data1 = "Was it a car or a cat I saw?"
        expected_output1 = True
        test_data2 = "tab a cat"
        expected_output2 = False
        test_data3 = " "
        expected_output3 = True

        obj = IsPalindrome()

        self.assertEqual(obj.sol1(test_data1), expected_output1)
        self.assertEqual(obj.sol1(test_data2), expected_output2)
        self.assertEqual(obj.sol1(test_data3), expected_output3)

    def test_sol2(self):
        test_data1 = "Was it a car or a cat I saw?"
        expected_output1 = True
        test_data2 = "tab a cat"
        expected_output2 = False
        test_data3 = " "
        expected_output3 = True

        obj = IsPalindrome()

        self.assertEqual(obj.sol2(test_data1), expected_output1)
        self.assertEqual(obj.sol2(test_data2), expected_output2)
        self.assertEqual(obj.sol2(test_data3), expected_output3)