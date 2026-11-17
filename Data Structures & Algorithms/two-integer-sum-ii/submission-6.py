class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complements = {}
        l, r = 0, len(numbers) - 1

        for i in range(len(numbers)):
            num = numbers[i]
            complements[num] = target - num
            while r > 0 and numbers[r] > complements[num]:
                r -= 1
            if numbers[r] == complements[num]:
                return [i+1, r+1]
            r = len(numbers) - 1
