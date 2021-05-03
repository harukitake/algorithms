h, w = map(int, input().split())

A = list()
for i in range(h):
    line = list(map(int, input().split()))
    A.append(line)

col_sum = [0] * h
row_sum = [0] * w
for i in range(h):
    for j in range(w):
        col_sum[i] += A[i][j]
        row_sum[j] += A[i][j]

ans = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        ans[i][j] = str(col_sum[i] + row_sum[j] - A[i][j])


for i in range(h):
    print(' '.join(ans[i]))


