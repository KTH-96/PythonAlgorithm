from collections import defaultdict, deque
from typing import List


def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if not edges:
        return True

    path = defaultdict(list)

    for edge in edges:
        path[edge[0]].append(edge[1])
        path[edge[1]].append(edge[0])

    visit_node = set()
    q = deque()
    q.append(source)
    while q:
        node = q.popleft()
        if node == destination:
            return True
        if node in visit_node:
            continue
        visit_node.add(node)
        for x in path[node]:
            if x == destination:
                return True
            if x not in visit_node:
                q.append(x)

    return False


n = 3
edges = []
source = 0
destination = 2
validPath(n, edges, source, destination)
