import unittest
from ..products_of_array_discluding_self import ProductsOfArrayDiscludingSelf

class TestProductsOfArrayDiscludingSelf(unittest.TestCase):

    def test_products_of_array_discluding_self_1(self):
        # Arrange
        input1 = [1 , 2, 4, 6]
        expected_output1 = [48, 24, 12, 8]
        input2 = [-1, 0, 1, 2, 3]
        expected_output2 = [0,-6,0,0,0]
        input3 = [0, 0]
        expected_output3 = [0, 0]
        obj = ProductsOfArrayDiscludingSelf()

        # Execute
        actual_output1 = obj.products_of_array_discluding_self_1(input1)
        actual_output2 = obj.products_of_array_discluding_self_1(input2)
        actual_output3 = obj.products_of_array_discluding_self_1(input3)

        # Compare
        self.assertEqual(expected_output1, actual_output1)
        self.assertEqual(expected_output2, actual_output2)
        self.assertEqual(expected_output3, actual_output3)

    def test_products_of_array_discluding_self_2(self):
        # Arrange
        input1 = [1, 2, 4, 6]
        expected_output1 = [48, 24, 12, 8]
        input2 = [-1, 0, 1, 2, 3]
        expected_output2 = [0, -6, 0, 0, 0]
        input3 = [0, 0]
        expected_output3 = [0, 0]
        obj = ProductsOfArrayDiscludingSelf()

        # Execute
        actual_output1 = obj.products_of_array_discluding_self_2(input1)
        actual_output2 = obj.products_of_array_discluding_self_2(input2)
        actual_output3 = obj.products_of_array_discluding_self_2(input3)

        # Compare
        self.assertEqual(expected_output1, actual_output1)
        self.assertEqual(expected_output2, actual_output2)
        self.assertEqual(expected_output3, actual_output3)
