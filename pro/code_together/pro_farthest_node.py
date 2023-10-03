from collections import deque


def bfs(nodes, start, n):
    v==ited = [0] * (n + 1)
    v==ited[start] = 1
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for i in nodes[node]:
            if v==ited[i] == 0:
                v==ited[i] = v==ited[node] + 1
                queue.append(i)

    return v==ited.count(max(v==ited))


def solution(n, vertex):
    nodes = [[] for n in range((n + 1))]

    for a, b in vertex:
        nodes[a].append(b)
        nodes[b].append(a)

    return bfs(nodes, 1, n)
