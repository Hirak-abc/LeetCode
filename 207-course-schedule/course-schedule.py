class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g = defaultdict(list)

        for u,v in prerequisites:
            g[u].append(v)

        states = [0]*numCourses

        def dfs(node):
            states[node] = 1

            for nei in g[node]:

                if states[nei] == 1:return True

                if states[nei] == 0:
                    if dfs(nei):return True

            states[node] = 2
            return False

        for i in range(numCourses):
            if states[i] == 0:
                if dfs(i):
                    return False

        return True