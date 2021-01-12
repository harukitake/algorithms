WHITE = 0 # 訪問前
GRAY = 1 # 訪問中
BLACK = 2 # 訪問済
def dfs(i: int, n: int):
    nt = [0] * n
    time_list = [0] * n
    
    return i


n = int(input())
for i in range(n):
    matrix_info = list(map(int, input().split()))

    if matrix_info[1] > 0:
        for j in range(2, len(matrix_info)):
            adj_matrix[matrix_info[0] - 1][matrix_info[j] - 1] = 1

process = [WHITE] * n
next_node = [0] * n

for i in range(n):
    if process[i] == WHITE:
        dfs(i, n)
