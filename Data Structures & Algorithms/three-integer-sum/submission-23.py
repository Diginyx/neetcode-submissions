class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()
        for i in range(len(nums)):
            num = nums[i]
            temp = 0 - num
            l, r = i+1, len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum > temp:
                    r -= 1
                elif curr_sum < temp:
                    l += 1
                else:
                    output.add((num, nums[l], nums[r]))
                    r -= 1
                    l += 1
        return [list(x) for x in output]
        