class ThreeSums:

    def sol1(self, nums: list[int]) -> list[[int]]:
        res = []
        nums.sort()

        for i, v in enumerate(nums):

            if v > 0:
                break

            # avoid using duplicate value. check starts from index 2
            if i > 0 and v == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                three_sums = v + nums[l] + nums[r]
                if three_sums > 0:
                    r -= 1
                elif three_sums < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


