import unittest
from ..longest_consecutive_sequence import LongestConsecutiveSequence

class TestLongestConsecutiveSequence(unittest.TestCase):

    def test_sol1(self):

        test_data1 =  [2,20,4,10,3,4,5]
        expected_result1 = 4
        test_data2 = [0,3,2,5,4,6,1,1]
        expected_result2 = 7

        obj = LongestConsecutiveSequence()

        self.assertEqual(obj.sol1(test_data1), expected_result1)
        self.assertEqual(obj.sol1(test_data2), expected_result2)


