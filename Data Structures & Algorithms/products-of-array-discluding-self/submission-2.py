class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finalArr = [0] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            finalArr[i] = prefix      # everything before i (before we include nums[i])
            prefix *= nums[i]         # now fold nums[i] in for the NEXT position

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            finalArr[i] *= suffix     # combine with the prefix already stored
            suffix *= nums[i]

        return finalArr