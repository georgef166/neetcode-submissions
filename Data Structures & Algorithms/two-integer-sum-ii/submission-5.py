class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        initial = 0
        answer = []

        while initial < len(numbers):
            for i in range(len(numbers)):
                if numbers[initial] + numbers[i] == target:
                    answer.append(initial + 1)
                    answer.append(i + 1)
                    return answer

            left += 1
                