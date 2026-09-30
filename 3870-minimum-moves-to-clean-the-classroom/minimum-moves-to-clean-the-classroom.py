from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])

        start = None
        litter = {}
        k = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = k
                    k += 1

        full = (1 << k) - 1

        # best[r][c][mask] = maximum energy seen
        best = [[[-1] * (1 << k) for _ in range(n)] for _ in range(m)]

        q = deque()
        q.append((start[0], start[1], energy, 0, 0))
        best[start[0]][start[1]][0] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, e, mask, steps = q.popleft()

            if mask == full:
                return steps

            if e == 0:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                ne = e - 1
                nmask = mask

                if classroom[nr][nc] == 'L':
                    nmask |= 1 << litter[(nr, nc)]

                if classroom[nr][nc] == 'R':
                    ne = energy

                # Already reached this state with >= energy
                if best[nr][nc][nmask] >= ne:
                    continue

                best[nr][nc][nmask] = ne
                q.append((nr, nc, ne, nmask, steps + 1))

        return -1