class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        window_sum = sum(arr[:k])
        ans = 0

        if window_sum >= k * threshold:
            ans += 1

        for i in range(k,len(arr)):
            window_sum = window_sum - arr[i-k] + arr[i]
            if window_sum/k >= threshold: ans+=1

        return ans