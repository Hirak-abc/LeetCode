class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = Counter(arr)

        return len(count.values()) == len(set(count.values()))