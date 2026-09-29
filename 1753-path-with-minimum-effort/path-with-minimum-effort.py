class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        n = len(heights)
        m = len(heights[0])

        INF = float('inf')

        dist = [[INF]*m for _ in range(n)]
        dist[0][0] = 0

        pq = [(0,0,0)]

        directions = [(1,0),(-1,0),(0,-1),(0,1)]

        while pq:
            effort,row,column = heapq.heappop(pq)

            if dist[row][column] != effort:continue

            if row == n-1 and column == m-1:return effort

            for dr,dc in directions:
                nr = row + dr
                nc = column +  dc

                if 0<=nr<n and 0<=nc<m:
                    diff = abs(heights[row][column] - heights[nr][nc])

                    new_effort = max(effort,diff)

                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(pq,(new_effort,nr,nc))