n, m = map(int, input().split())

# 繋がりを保存
connect = [[] for _ in range(m)]
for _ in range(m):
    s, t = map(int, input().split())
    connect[s].append(t)
    connect[t].append(s)


# TODO dps()