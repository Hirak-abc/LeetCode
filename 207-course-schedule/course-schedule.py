class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g = defaultdict(list)
        courses = prerequisites

        for a,b in courses:
            g[a].append(b)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED]*numCourses

        def dfs(node):
            state = states[node]
            if state == VISITED:return True
            if state == VISITING:return False

            states[node] = VISITING

            for nei in g[node]:
                if not dfs(nei):return False
            
            states[node] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True