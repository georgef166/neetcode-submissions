class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = 1

        answer = []

        while left < len(numbers):
            if numbers[left] + numbers[right] == target:
                answer.append(numbers[left])
                answer.append(numbers[right])
                break
            else:
                left = right
                right = left + 1

        return answer
                