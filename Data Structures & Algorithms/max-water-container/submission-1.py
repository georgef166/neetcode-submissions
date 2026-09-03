class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxSize = 0

        while l < r:
            currentBox = min(heights[l], heights[r]) * (r - l)
            if currentBox > maxSize:
                maxSize = currentBox
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return maxSize