before_sort = [3, 7, 0, 1, 4, 7, 6, 20, 333, 5, 3]


def bubble_sort(target: list) -> list:
    """
    バブルソート
    大きい値が最後から順に決まっていくイメージ
    :param target:
    :return:
    """
    # i番目までソート済み
    for i in range(len(target)):
        for j in range(len(target) - i - 1):
            if target[j] > target[j + 1]:
                target[j], target[j + 1] = target[j + 1], target[j]
    return target


print(bubble_sort(before_sort))
