before_sort = [4, 6, 7, 2, 4, 8, 9, 1, 3]


def merge_sort(target: list) -> list:
    """
    マージソート
    分割統治法を使って半分に分けてソートしていく
    NlogN
    :param target:
    :return:
    """
    # 分割する
    if len(target) <= 1:
        return target

    # 真ん中
    mid = len(target) // 2

    # 分割
    left = target[:mid]
    right = target[mid:]

    # 再帰的に分割してソートしていく
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left: list, right: list) -> list:
    """
    ソートされた配列をマージする
    :param left:
    :param right:
    :return:
    """
    merged = []
    left_index, right_index = 0, 0

    # どちらかを入れ切るまで小さい方を入れていく
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # 片方が余ってしまうので残りを入れる
    if left_index < len(left):
        merged.extend(left[left_index:])

    if right_index < len(right):
        merged.extend(right[right_index:])

    return merged


print(merge_sort(before_sort))
