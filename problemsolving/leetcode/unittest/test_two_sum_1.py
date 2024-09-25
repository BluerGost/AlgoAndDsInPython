import unittest

from ..two_sum_1 import TwoSums


class TestTwoSum(unittest.TestCase):

    def test_sol1(self):

        nums1 = [2,7,11,15]
        target1 = 9
        output1 = [0,1]

        nums2 = [3, 2, 4]
        target2 = 6
        output2 = [1,2]

        nums3 = [3, 3]
        target3 = 6
        output3 = [0,1]

        obj = TwoSums()
        self.assertEqual(output1, obj.sol1(nums1, target1))
        self.assertEqual(output2, obj.sol1(nums2, target2))
        self.assertEqual(output3, obj.sol1(nums3, target3))