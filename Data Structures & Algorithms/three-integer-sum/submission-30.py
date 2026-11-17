class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

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
                    output.append([num, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # while l < r and nums[r] == nums[r + 1]:
                    #     r -= 1
        return output
        