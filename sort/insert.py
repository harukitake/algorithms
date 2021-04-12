before_sort = [4, 6, 2, 7, 5]


def insert_sort(target: list) -> list:
    """
    選択ソート
    ソート済みの部分で入る場所を探していく
    :param target:
    :return:
    """
    # i−1番目までが整理済み
    for i in range(len(target)):
        val = target[i]
        j = i - 1
        # i番目がどこに入るか考える
        # ソート済みのi-1番めまででi番目がどこに入るか考える
        # i番目より大きい場合はずらしていく
        while j >= 0 and target[j] > val:
            target[j + 1] = target[j]
            j -= 1
        # i番目を代入
        target[j + 1] = val

    return target


after_sort = insert_sort(before_sort)
print(after_sort)





