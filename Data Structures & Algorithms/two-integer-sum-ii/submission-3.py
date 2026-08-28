class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = 1

        answer = []

        while left < len(numbers):
            for i in range(len(numbers)):
                if left + numbers[i] == target:
                    answer.append(left + 1)
                    answer.append(i)
                    return answer

            left += 1

                