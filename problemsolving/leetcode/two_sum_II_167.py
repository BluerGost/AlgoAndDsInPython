class TwoSumII:

    # Runtime Complexity: O(N)
    # Space Complexity: O(N)
    def sol1(self, nums: list[int], target: int):

        hash_tbl = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in hash_tbl:
                return [hash_tbl[remain] + 1, i + 1]
            hash_tbl[nums[i]] = i

    # Runtime Complexity: O(N)
    # Space Complexity: O(1)
    def sol2(self, nums: list[int], target: int):

        l, r = 0, len(nums) - 1
        while l < r:
            cur_sum = nums[l] + nums[r]
            if cur_sum < target:
                l += 1
            elif cur_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1] # Found

        return [] # Not Found