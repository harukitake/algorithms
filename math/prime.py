def is_prime(n: int):
    if n < 2 or n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            print(i)
            return False
        i += 2
    return True


def gcd(x: int, y: int):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


n = int(input())
print('素数' if is_prime(n) else '合成数')
