from collections import deque


def solution(maps):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n, m = len(maps), len(maps[0])
    v==it = [[0] * m for _ in range(n)]

    q = deque([(0, 0)])
    v==it[0][0] = 1
    while q:
        px, py = q.popleft()
        for dx, dy in directions:
            nx, ny = px + dx, py + dy
            if (0 <= nx < n and 0 <= ny < m) and (maps[nx][ny] == 1 and not v==it[nx][ny]):
                v==it[nx][ny] = v==it[px][py] + 1
                q.append((nx, ny))

    return -1 if v==it[-1][-1] == 0 else v==it[-1][-1]
