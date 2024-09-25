class TwoSumII:

    def sol1(self, nums: list[int], target: int):

        hash_tbl = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in hash_tbl:
                return [hash_tbl[remain] + 1, i + 1]
            hash_tbl[nums[i]] = i