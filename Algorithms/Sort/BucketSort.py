class BucketSort:
    def __init__(self):
        pass

    def InsertSort(self, nums: list[float]) -> list[float]:
        numsLen = len(nums)

        for currIndex in range(1, numsLen):
            prevIndex = currIndex - 1
            currValue = nums[currIndex]

            while prevIndex >= 0 and nums[prevIndex] > currValue:
                nums[prevIndex + 1] = nums[prevIndex]
                prevIndex -= 1

            nums[prevIndex + 1] = currValue

    def Sort(self, nums:list[float]) -> list[float]:

        numLen = len(nums)
        buckets = [[] for _ in range(numLen)]


        # Step-1, Seperate the items in different buckets
        for num in nums:
            bucketIndex = int(num * numLen)
            buckets[bucketIndex].append(num)

        # Step-2, Sort the individual buckets
        for bucket in buckets:
            self.InsertSort(bucket)

        # Step-3, Merge the sorted buckets into a single list
        numsIndex = 0
        for bucket in buckets:
            for num in bucket:
                nums[numsIndex] = num
                numsIndex += 1


