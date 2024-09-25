class TwoSums:

    def sol1(self, nums: list[int], target: int) -> list[int]:

        hash_tbl = {}

        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in hash_tbl:
                return [i, hash_tbl[remain]]
            hash_tbl[nums[i]] = i


