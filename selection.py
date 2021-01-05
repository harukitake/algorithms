n = int(input())
A = list(map(int, input().split()))

def selectionSort(arr: list, n: int):
    count = 0
    for i in range(n):
        minKey = i
        for j in range(i, n):
            if arr[j] < arr[minKey]:
                minKey = j
        arr[i], arr[minKey] = arr[minKey], arr[i]

        if minKey != i:
            count += 1
    return arr, count

sortedList, swapCount = selectionSort(A, n)
print(' '.join(map(str, sortedList)))
print(swapCount)
    
