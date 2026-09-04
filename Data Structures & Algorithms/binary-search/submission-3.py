class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1 ,2 3, 5, 7, 8, 9
        # target = 3

        l, r = 0, len(nums) -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1              
            elif nums[mid] > target:
                r = mid - 1
        
        return -1
