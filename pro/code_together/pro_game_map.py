from collections import deque


def solution(maps):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n, m = len(maps), len(maps[0])
    visit = [[0] * m for _ in range(n)]

    q = deque([(0, 0)])
    visit[0][0] = 1
    while q:
        px, py = q.popleft()
        for dx, dy in directions:
            nx, ny = px + dx, py + dy
            if (0 <= nx < n and 0 <= ny < m) and (maps[nx][ny] == 1 and not visit[nx][ny]):
                visit[nx][ny] = visit[px][py] + 1
                q.append((nx, ny))

    return -1 if visit[-1][-1] == 0 else visit[-1][-1]
