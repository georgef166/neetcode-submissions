class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [] * len(nums)
        
        i = 0

        while i < len(nums):
            currentVal = nums[i]
            newNumList = nums.pop(i)

            valMul = 1
            for num in nums:
                valMul = valMul * num
            
            output.append(valMul)
            nums.insert(0, currentVal)
            i+=1


        return output