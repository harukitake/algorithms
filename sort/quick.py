before_sort = [4, 5, 1, 3, 0, 2, 9, 6, 7, 8, 12, 8]


def quick_sort(target: list) -> list:
    """
    クイックソート
    分割統治法を使う
    partitionにより前後に分割し再帰的にソートしていく
    :param target:
    :return:
    """
    if len(target) <= 1:
        return target

    # データの初期状態に左右されないためにrandom.choiceを使うこともあるらしい
    # standard = random.choice(len(target))
    partition_arr, standard_index = partition(target, len(target) - 1, 0)

    left = partition_arr[:standard_index]
    right = partition_arr[standard_index:]

    left = quick_sort(left)
    right = quick_sort(right)

    return left + right


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


print(quick_sort(before_sort))