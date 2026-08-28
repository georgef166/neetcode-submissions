class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finalArr = [0] * len(nums)
        for i, n in enumerate(nums):
            j = 0
            currentMul = 1
            while j < i:
                currentMul = currentMul * nums[j]
                j += 1
            j = len(nums) - 1
            while j > i:
                currentMul = currentMul * nums[j]
                j -= 1 
            finalArr[i] = currentMul
        return finalArr
        










