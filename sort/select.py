before_sort = [3, 2, 1, 1, 10, 7, 6, 8, 5]


def select_sort(target: list) -> list:
    """
    選択ソート
    最小値をさがして挿入していく
    :param target:
    :return:
    """

    # i番目までがソート済み
    for i in range(len(target)):
        min_j = i
        for j in range(i, len(target)):
            # 最小値を見つける
            if target[j] < target[min_j]:
                min_j = j
        target[i], target[min_j] = target[min_j], target[i]
    return target


print(select_sort(before_sort))

