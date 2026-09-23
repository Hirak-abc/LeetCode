class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):

        g = defaultdict(list)

        for a, b in prerequisites:
            g[a].append(b)

        memo = {}

        def dfs(u, v):
            if (u, v) in memo:
                return memo[(u, v)]

            for x in g[u]:
                if x == v or dfs(x, v):
                    memo[(u, v)] = True
                    return True

            memo[(u, v)] = False
            return False

        return [dfs(u, v) for u, v in queries]