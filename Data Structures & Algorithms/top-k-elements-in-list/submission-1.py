class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        countNums = {}
        finalOutput = []

        for i in range(len(nums)):
            countNums[nums[i]] = 1 + countNums.get(nums[i], 0)

        j = 0
        while j < k:
            biggestCount = 0
            for c in countNums:
                if biggestCount < countNums[c]:
                    biggestCount = c
            finalOutput.append(biggestCount)
            countNums.pop(biggestCount, None)
            j+=1

        return finalOutput



        # count_S, count_T = {}, {}

        # for i in range(len(s)):
        #     count_S[s[i]] = 1 + count_S.get(s[i], 0)
        #     count_T[t[i]] = 1 + count_T.get(t[i], 0)     
        # for c in count_S:
        #     if countS[c] != countT.get(c, 0):
        #         return False

        # return True       