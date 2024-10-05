import unittest
from ..two_sum_II_167 import TwoSumII

class TestTwoSum(unittest.TestCase):

    def test_sol1(self):

        nums1 = [2,7,11,15]
        target1 = 9
        output1 = [1,2]

        nums2 = [2, 3, 4]
        target2 = 6
        output2 = [1, 3]

        nums3 = [-1, 0]
        target3 = -1
        output3 = [1, 2]

        obj = TwoSumII()
        self.assertEqual(output1, obj.sol1(nums1, target1))
        self.assertEqual(output2, obj.sol1(nums2, target2))
        self.assertEqual(output3, obj.sol1(nums3, target3))

    def test_sol2(self):

        nums1 = [2,7,11,15]
        target1 = 9
        output1 = [1,2]

        nums2 = [2, 3, 4]
        target2 = 6
        output2 = [1, 3]

        nums3 = [-1, 0]
        target3 = -1
        output3 = [1, 2]

        obj = TwoSumII()
        self.assertEqual(output1, obj.sol2(nums1, target1))
        self.assertEqual(output2, obj.sol2(nums2, target2))
        self.assertEqual(output3, obj.sol2(nums3, target3))