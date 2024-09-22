class TopKFrequentElements:
    def Run(self, nums: list[int], k: int) -> list[int]:

        freqCountDict = {}
        for num in nums:
            freqCountDict[num] = freqCountDict.get(num, 0) + 1

        bucketList = [[] for _ in range(len(nums) + 1)]
        for num, freq in freqCountDict.items():
            bucketList[freq].append(num)

        topKElementList = []
        for bucket in reversed(bucketList):
            for num in bucket:
                topKElementList.append(num)
                if len(topKElementList) == k:
                    return topKElementList
