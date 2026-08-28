class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = 1

        answer = []

        while left < len(numbers) and right < len(numbers):
            if numbers[left] + numbers[right] == target:
                answer.append(left + 1)
                answer.append(right + 1)
                break
            else:
                left = right
                right = left + 1

        return answer
                