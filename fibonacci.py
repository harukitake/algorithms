def fib(n: int):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fibDynamic(n: int):
    fibSequence = {}

    fibSequence[0] = fibSequence[1] = 1

    if n == 1 or n == 2:
        return fibSequence[0]

    for i in range(2, n + 1):
        fibSequence[i] = fibSequence[i - 1] + fibSequence[i - 2]

    return fibSequence[n]


n = int(input())

print('{}'.format(str(fibDynamic(n))))
print('{}'.format((str(fib(n)))))