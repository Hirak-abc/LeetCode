class Solution:
    def findMinHeightTrees(self, n, edges):
        if n <= 2:
            return list(range(n))

        g = defaultdict(list)
        deg = [0] * n

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            deg[u] += 1
            deg[v] += 1

        q = deque(i for i in range(n) if deg[i] == 1)

        while n > 2:
            n -= len(q)

            for _ in range(len(q)):
                u = q.popleft()

                for v in g[u]:
                    deg[v] -= 1
                    if deg[v] == 1:
                        q.append(v)

        return list(q)