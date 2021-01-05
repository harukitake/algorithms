def getLcs(x: list, y: list):
    a = len(x)
    b = len(y)
    z = [[0] * (b + 1) for _ in range(a + 1)]
    
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if x[i - 1] == y[j - 1]:
                z[i][j] = z[i - 1][j - 1] + 1
            else:
                z[i][j] = max([z[i - 1][j], z[i][j - 1]])
    return z[i][j]

n = int(input())

for _ in range(n):
    a = input()
    b = input()
    print(getLcs(a, b))