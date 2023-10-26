from collections import deque
from typing import List


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    n = len(grid)
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1

    visited = [[0 for _ in range(n)] for _ in range(n)]

    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    grid[0][0] = 1
    while q:
        cn, cm = q.popleft()
        if cn == n - 1 and cm == n - 1:
            return grid[-1][-1]

        for nn, nm in [[cn - 1, cm], [cn + 1, cm], [cn + 1, cm + 1], [cn + 1, cm - 1],
                       [cn, cm - 1], [cn, cm + 1], [cn - 1, cm - 1], [cn - 1, cm + 1]]:
            if (0 <= nn < n and 0 <= nm < n and grid[nn][nm] == 0 and visited[nn][nm] != 1):
                grid[nn][nm] = grid[cn][cm] + 1
                q.append((nn, nm))
                visited[nn][nm] = 1

    return -1


grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print(shortestPathBinaryMatrix(grid))
