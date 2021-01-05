n = int(input())

adj_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    matrix_info = list(map(int, input().split()))

    if matrix_info[1] > 0:
        for j in range(2, len(matrix_info)):
            adj_matrix[matrix_info[0] - 1][matrix_info[j] - 1] = 1

for i in range(n):
    print(' '.join(map(str, adj_matrix[i])))


