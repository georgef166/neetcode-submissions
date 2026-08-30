class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #List[int] == [1, 2, 3, 4, 6]
                    #  1  2  3  4  5
        #target == 3

        #Result[int] == [1, 2]


        numSet = set(numbers)
        index1 = 0
        index2 = 0
        val2 = 0
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in numSet:
                index1 = i
                val2 = diff
            if n == diff:
                index2 = i
        
        return [min(index1 + 1, index2 + 1), max(index1 + 1, index2 + 1)]
