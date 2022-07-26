from collections import deque


def solution(maps):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visit = [[0] * len(maps[0]) for _ in range(len(maps))]

    q = deque([(0, 0)])
    visit[0][0] = 1
    while q:
        px, py = q.popleft()
        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = visit[px][py] + 1
                    q.append((nx, ny))

    if visit[-1][-1] == 0:
        return -1
    return visit[-1][-1]


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
