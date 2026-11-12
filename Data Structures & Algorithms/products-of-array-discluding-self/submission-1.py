class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
            elif i == 1:
                prefix[i] = nums[i-1]
            else: 
                prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suffix[i] = 1
            elif i == len(nums)-2:
                suffix[i] = nums[i+1]
            else: 
                suffix[i] = suffix[i+1] * nums[i+1]
        multiplied = [a * b for a, b in zip(prefix, suffix)]    
        
        return multiplied