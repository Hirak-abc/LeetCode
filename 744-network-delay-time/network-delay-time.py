class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        g = defaultdict(list)
        for u,v,w in times:
            g[u].append((v,w))

        INF = float('inf')
        dist = [INF]*(n+1)
        dist[k] = 0

        pq = [(0,k)]

        while pq:
            d,u = heapq.heappop(pq)

            if d!=dist[u]:continue

            for v,w in g[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
        ans = max(dist[1:])

        if ans == INF:
            return -1

        return ans


