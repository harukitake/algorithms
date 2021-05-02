# 2分探索
# 最小値の最大化 -> 2分探索で溶けることが多い
# k + 1個以上の長さM以上のピースに分割可能か？ という判定問題に言い換える

n, l = map(int, input().split())
k = int(input())
splits = list(map(int, input().split()))


# 長さmのピースに分割可能か？
# 貪欲法
# 0 が条件を満たすこともあるので-1から
# 分割できる
left = -1
# 分割できない
right = l + 1

mid = 0
# 最大の長さを求める
while right - left > 1:
    mid = left + (right - left) // 2
    # check
    # 切れ目の数
    count = 0
    # 一つ前の切れ目
    pre = 0
    can_split = False
    for i in range(n):
        # 長さm以上で分割できるかを判定していく
        # 長さmを超えたら分割する
        # 最後は端も長さm以上出ないといけないの二つ目の条件も考える必要がある
        if splits[i] - pre >= mid and l - splits[i] >= mid:
            count += 1
            pre = splits[i]

    if count >= k:
        can_split = True

    if can_split:
        left = mid
    else:
        right = mid

print(left)

