import queue
n = int(input())

way_list = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    way_list[a].append(b)
    way_list[b].append(a)


INF = float('inf')


def get_depth_list(start: int) -> list:
    """
    幅優先探索で最短距離を計算
    :param start:
    :return:
    """
    dist = [INF] * (n + 1)
    q = queue.Queue()
    q.put(start)
    dist[start] = 0

    while not q.empty():
        current = q.get()
        for to in way_list[current]:
            if dist[to] == INF:
                dist[to] = dist[current] + 1
                q.put(to)

    return dist


# 頂点1からの最短距離を求める
# その過程で頂点1からもっとも離れている頂点を求める
dist = get_depth_list(1)
max_depth_1, max_id_1 = -1, -1
for i, d in enumerate(dist):
    if INF != d and max_depth_1 < d:
        max_depth_1 = d
        max_id_1 = i


# 上で求めた頂点1からもっとも離れている頂点から木の直径を求める
dist = get_depth_list(max_id_1)
max_depth_2 = -1
for d in dist:
    if d != INF:
        max_depth_2 = max(max_depth_2, d)


# 木の直径に辺を一本足して閉路としたものが答え
print(max_depth_2 + 1)

