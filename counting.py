n = int(input())
A = list(map(int, input().split()))
k = 10000

def countingSort(arr: list, k: int, n: int):
    c = [0] * k
    for j in range(n):
        c[arr[j]] += 1
    
    for i in range(1, k):
        c[i] = c[i] + c[i - 1]
        
    for i in range(n - 1, 0, -1):
        arr[c[arr[i]]] = arr[i]
        c[arr[i]] -= 1
    return arr

arr = countingSort(A, k, n)
print(' '.join(map(str, arr)))