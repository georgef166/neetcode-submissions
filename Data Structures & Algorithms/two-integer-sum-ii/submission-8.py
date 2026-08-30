class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #List[int] == [1, 2, 3, 4, 6]
                    #  1  2  3  4  5
        #target == 3

        #Result[int] == [1, 2]
        l = 0 
        r = len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            elif s > target:
                r -= 1

        return [l, r]