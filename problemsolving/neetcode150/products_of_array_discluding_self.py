from sys import prefix


class ProductsOfArrayDiscludingSelf:

    # Time Complexity: O(3n) = O(n), Runtime Complexity: O(4n) = O(n)
    def products_of_array_discluding_self_1(self, nums: list[int]) -> list[int]:

        prefix_mul = [nums[0]]
        for i in range(1, len(nums)):
            prefix_mul.append(prefix_mul[i-1] * nums[i])

        postfix_mul = [nums[len(nums) - 1]]
        for i in range(len(nums) - 2, -1, -1):
            postfix_mul.insert(0, postfix_mul[0] * nums[i])

        res = []
        for i in range(len(nums)):
            left = 1
            right = 1
            if i != 0:
                left = prefix_mul[i - 1]
            if i != len(nums) - 1:
                right = postfix_mul[i + 1]
            res.append(left * right)

        return res

    def products_of_array_discluding_self_2(self, nums: list[int]) -> list[int]:

        res = [1]
        for i in range(len(nums) - 1):
            res.append(res[i] * nums[i])
        print(res)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res

