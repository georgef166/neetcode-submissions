class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:    
        countNums = {}
        finalOutput = []

        for i in range(len(nums)):
            countNums[nums[i]] = 1 + countNums.get(nums[i], 0)

        j = 0
        while j < k:
            biggestCount = 0
            biggestVal = 0
            for c in countNums:
                if biggestCount < countNums[c]:
                    biggestCount = countNums[c]
                    biggestVal = c
            finalOutput.append(biggestVal)
            countNums.pop(biggestVal)
            j+=1

        return finalOutput


        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        # for n, c in count.items():
        #     freq[c].append(n)

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res






