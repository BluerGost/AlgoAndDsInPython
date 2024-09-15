class InsertionSort:
    def __init__(self):
        pass

    def Sort(self, nums:list[float]) -> list[float]:
        numsLen = len(nums)

        for currIndex in range(1, numsLen):
            prevIndex = currIndex - 1
            currValue = nums[currIndex]

            while prevIndex >= 0 and nums[prevIndex] > currValue:
                nums[prevIndex + 1] = nums[prevIndex]
                prevIndex -= 1

            nums[prevIndex + 1] = currValue




