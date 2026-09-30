class Solution(object):
    def eventualSafeNodes(self, graph):

        n = len(graph)
        states = [0] * n
        safe = []

        def dfs(node):
            # Currently in recursion path
            if states[node] == 1:
                return False

            # Already determined
            if states[node] == 2:
                return True

            if states[node] == 3:
                return False

            states[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    states[node] = 3
                    return False

            states[node] = 2
            return True

        for i in range(n):
            if dfs(i):
                safe.append(i)

        return safe