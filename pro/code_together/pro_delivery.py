import heapq


def dijkstra(graph, distance):
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        else:
            distance[now] = dist
        print(distance)
        print(dist)
        for b, c in graph[now]:
            print(b,c)
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(q, (cost, b))



def solution(N, road, K):
    distance = [float('inf')] * (N + 1)
    graph = [[] for _ in range(N + 1)]

    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    print(graph)
    dijkstra(graph, distance);
    return len([dist for dist in distance if dist <= K])


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
