class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1  2  4  8
        #10 11 12 13
        #14 20 30 40


        top, bot = 0, len(matrix) - 1
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                l, r = 0, len(matrix[0]) - 1
                while l <= r:
                    mid2 = (l + r) // 2
                    if target == matrix[mid][mid2]:
                        return True
                    elif target > matrix[mid][mid2]:
                        l = mid2 + 1
                    elif target < matrix[mid][mid2]:
                        r = mid2 - 1
                return False
        return False