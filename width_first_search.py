import queue

n = int(input())
# 隣接行列
adj_matrix = [[False] * n for _ in range(n)]
for i in range(n):
    matrix_info = list(map(int, input().split()))

    if matrix_info[1] > 0:
        for j in range(2, len(matrix_info)):
            adj_matrix[matrix_info[0] - 1][matrix_info[j] - 1] = True

# 距離
CANT_ARRIVE = -1

def wfs(i: int):
    q = queue.Queue()
    q.put(i)
    distance = [CANT_ARRIVE] * n
    distance[i] = 0
    while not q.empty():
        current_num = q.get()
        # current_item に隣接する点探す
        # 距離 + 1
        for j in range(n):
            # 隣接してない点は飛ばす
            if not adj_matrix[current_num][j]: continue
            # 計算済みの点は飛ばす
            if distance[j] != CANT_ARRIVE: continue
            distance[j] = distance[current_num] + 1
            q.put(j)
    return distance

distance = wfs(0)

for i in range(n):
    print('{} {}'.format(i + 1, distance[i]))
