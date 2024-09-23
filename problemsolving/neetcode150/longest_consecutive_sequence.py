class LongestConsecutiveSequence:

    def sol1(self, nums: list[int]) -> list[int]:

        nums_set = set(nums)
        longest_seq = 0

        for num in nums_set:
            # If the starting item of a sequence
            if (num - 1) not in nums_set:
                current_seq = 0
                while (num + current_seq) in nums_set:
                    current_seq += 1
                longest_seq = max(longest_seq, current_seq)

        return  longest_seq



