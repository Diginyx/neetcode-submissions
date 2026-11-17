class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        output = set()
        for i in range(len(nums_sorted)):
            num = nums_sorted[i]
            temp = 0 - num
            l, r = i+1, len(nums) - 1
            count = 0
            while l < r:
                curr_sum = nums_sorted[l] + nums_sorted[r]
                if curr_sum > temp:
                    r -= 1
                elif curr_sum < temp:
                    l += 1
                else:
                    output.add((num, nums_sorted[l], nums_sorted[r]))
                    r -= 1
                    l += 1
        return [list(x) for x in output]
        