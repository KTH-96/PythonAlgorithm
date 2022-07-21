from collections import deque


def bfs(nodes, start, n):
    visited = [0] * (n + 1)
    visited[start] = 1
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for i in nodes[node]:
            if visited[i] == 0:
                visited[i] = visited[node] + 1
                queue.append(i)

    return visited.count(max(visited))


def solution(n, vertex):
    nodes = [[] for n in range((n + 1))]

    for a, b in vertex:
        nodes[a].append(b)
        nodes[b].append(a)

    return bfs(nodes, 1, n)
