from collections import deque
from typing import List


class NumberOfIslands200:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        size = 0

        def bfs(x, y):
            q = deque()
            q.append((x, y))
            visited[x][y] = 1
            while q:
                x, y = q.popleft()
                for nx, ny in [x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]:
                    if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                        continue

                    if grid[nx][ny] == '1' and visited[nx][ny] == 0:
                        q.append((nx, ny))
                        visited[nx][ny] = 1

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == '1' and visited[x][y] == 0:
                    print(x, y)
                    bfs(x, y)
                    size += 1

        return size


NumberOfIslands200.numIslands(NumberOfIslands200, [["0", "1", "0"], ["1", "0", "1"], ["0", "1", "0"]])
