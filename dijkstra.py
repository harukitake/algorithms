n = int(input())
INF = float('inf')

# 前処理
adj_matrix = [[INF] * n for _ in range(n)]
for _ in range(n):
    u, k, *edges_info = map(int, input().split())
    
    # 偶数番目、奇数番目に分けてそれを一組にする
    for v, cost in zip(edges_info[::2], edges_info[1::2]):
        adj_matrix[u][v] = cost

def dijkstra(n: int, adj_matrix: list):
    distance = [INF] * n
    parents = [-1] * n
    used = [False] * n

    distance[0] = 0
    while True:
        minv = INF
        u = -1
        for i in range(n):
            if minv > distance[i] and not used[i]:
                u = i
                minv = distance[i]

        if u == -1:
            break
        used[u] = True

        for j in range(n):
            if not used[j] and adj_matrix[u][j] != INF:
                if distance[u] + adj_matrix[u][j] < distance[j]:
                    distance[j] = distance[u] + adj_matrix[u][j]
                    parents[j] = u

    return distance

distance = dijkstra(n, adj_matrix)
for i in range(n):
    print(str(i) + ' ' + str(distance[i] if distance[i] != INF else -1))



