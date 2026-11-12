class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        countsArray = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for key, value in counts.items(): 
            countsArray[value].append(key)

        res = []
        for i in range(len(countsArray) - 1, 0, -1):
            for n in countsArray[i]:
                res.append(n)
                if len(res) == k:
                    return res