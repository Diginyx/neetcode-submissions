class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        topK = [0] * k

        for i in range(len(nums)):
            counts[nums[i]] = 1 + counts.get(nums[i], 0)

        # print(counts)
        sortedCounts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        # print(sortedCounts)
        for i in range(k):
            topK[i] = sortedCounts[i][0]
        return topK