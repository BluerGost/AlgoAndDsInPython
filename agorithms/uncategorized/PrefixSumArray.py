class PrefixSumArray:
    prefix_sum_list = []

    def __init__(self, nums: list[int]):
        self.prefix_sum_list.append(nums[0])
        for i in range(1, len(nums)):
            self.prefix_sum_list.append(self.prefix_sum_list[i-1] + nums[i])

    def print_prefix_sum(self):
        print(self.prefix_sum_list)