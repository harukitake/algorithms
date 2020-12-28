n = int(input())
A = list(map(int, input().split()))

def boubleSort(arr: list, n: int):
    count = 0
    flag = 1
    while flag:
        flag = 0
        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                flag = 1
                count += 1
    return arr, count

result, count = boubleSort(A, n)
print(' '.join(map(str, result)))
print(count)