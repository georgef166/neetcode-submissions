class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1 2 3 4 5 6 7

        # 6 7 1 2 3 4 5


        l, r = 0, len(nums) - 1

        mid = (l + r) //2

        return min(nums)

        