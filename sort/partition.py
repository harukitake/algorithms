before_partition = [4, 5, 12, 18, 11, 15, 7, 9, 10, 4, 2, 1, 3, 5, 6]


def partition(arr: list, r: int, p: int):
    """
    p番目の値より大きいか小さいかで分割する
    :param arr:
    :param r: 範囲の終わり 分割の基準
    :param p: 範囲の始まり
    :return:
    """
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return arr, i + 1


after_partition, standard_index = partition(before_partition, len(before_partition) - 1, 0)

after_partition[standard_index] = '[' + str(after_partition[standard_index]) + ']'
print(''.join(str(after_partition)))
