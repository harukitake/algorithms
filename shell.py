n = int(input())
A = list(map(int, input().split()))

def shellSort(arr: list, n: int):
    count = 0
    # 数列の生成
    sequence = getSequence(n)
    for i in sequence:
        arr, count = insertSort(arr, n, i, count)
    return arr, n

def insertSort(arr: list, n: int, g: int, count: int):
    count = 0
    for i in range(g, n):
        v = arr[i]
        j = i - g
        while j >= 0 and arr[j] > v:
            arr[j + g] = arr[j]
            j -= g
            count += 1
        arr[j + g] = v
    return arr, count


def getSequence(n: int):
    sequence = list()
    for i in range(n):
        if i > n: break
        i = 3 * i + 1
        sequence.append(3 * i + 1)
    return sequence