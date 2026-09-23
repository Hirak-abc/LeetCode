from collections import Counter

class Solution:
    def findShortestSubArray(self, nums):
        count = Counter(nums)
        degree = max(count.values())

        first = {}
        last = {}

        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i
            last[x] = i

        ans = len(nums)

        for x in count:
            if count[x] == degree:
                ans = min(ans, last[x] - first[x] + 1)

        return ans