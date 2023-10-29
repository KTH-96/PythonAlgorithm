from collections import deque
from typing import List


def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    if len(rooms) == 1 and len(rooms[0]) == 1:
        return True

    visited = [False for _ in range(len(rooms))]

    q = deque()
    q.append(0)

    while q:
        cx = q.popleft()
        visited[cx] = True
        for key in rooms[cx]:
            if not visited[key]:
                q.append(key)

    return all(visited)


rooms = [[1, 2], [2, 1], [1]]
print(canVisitAllRooms(rooms))
