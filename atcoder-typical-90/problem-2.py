# bit全探索

def check_valid(s: str) -> bool:
    count = 0

    for i in list(s):
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False

    if count == 0:
        return True

    return False


# 辞書式にかっこ列を出力する
n = int(input())

if n % 2 != 0:
    print()
else:
    # (か）のどちらであるかを01の羅列で考える 2** n 通り
    for i in range(2 ** n):
        # 候補となるカッコ列
        candidate = ''
        # 101011を右から 0か1かのどちらであるかをみていく
        for j in range(n - 1, -1, -1):
            # jだけシフト 10100 >> 2 = 101
            # j桁目が1であるか0であるかを判定
            if i >> j & 1 == 0:
                candidate += '('
            else:
                candidate += ')'

        if check_valid(candidate):
            print(candidate)


