def partition(arr: list, r: int, p: int):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return arr, i+1
