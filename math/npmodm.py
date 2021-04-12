def pow_mod(n: int, k: int, m: int) -> int:
    """
    繰り返し2乗法
    n: 底
    k: 乗数
    m: mod
    """
    if k == 0:
        return 1
    elif k % 2 == 1:
        # 奇数
        # n^k-1 * n をmで割ったあまり
        return pow_mod(n, k - 1, m) * n % m
    else:
        t = pow_mod(n, k // 2, m)
        return t * t % m


n, m, p = map(int, input().split())
print(pow_mod(n, p, m))
