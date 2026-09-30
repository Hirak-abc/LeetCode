class Solution(object):
    def longestCycle(self, edges):

        n = len(edges)
        seen = [-1] * n
        ans = -1
        time = 0

        for i in range(n):

            if seen[i] != -1:
                continue

            node = i
            start = time

            while node != -1 and seen[node] == -1:
                seen[node] = time
                time += 1
                node = edges[node]

            if node != -1 and seen[node] >= start:
                ans = max(ans, time - seen[node])

        return ans