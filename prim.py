n = int(input())

adj_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    items = list(map(int, input().split()))
    for j in range(n):
        adj_matrix[i][j] = items[j] if items[j] != -1 else float('inf')

def prim(n: int, adj_matrix: list):
    inf = float('inf')
    used = [False] * n
    costs = [inf] * n
    parents = [-1] * n

    costs[0] = 0

    while True:
        minv = inf
        u = -1 # 今調べている頂点のキー

        # まだ調べていない頂点を探す
        for i in range(n):
            if minv > costs[i] and not used[i]:
                minv = costs[i]
                u = i

        # 無くなったらやめる
        if u == -1:
            break

        used[u] = True
        for j in range(n):
            if not used[j] and adj_matrix[u][j] != inf:
                if costs[j] > adj_matrix[u][j]:
                    costs[j] = adj_matrix[u][j]
                    parents[j] = u

    sum_costs = 0
    for i in range(n):
        if parents[i] != -1:
            sum_costs += adj_matrix[i][parents[i]]

    return sum_costs

print(prim(n, adj_matrix))