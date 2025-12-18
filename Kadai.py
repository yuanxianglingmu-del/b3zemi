def Qsort(lst):
    # 要素が0個または1個ならそのまま返す
    if len(lst) <= 1:
        return lst

    # ピボットを先頭要素にする
    pivot = lst[0]

    # ピボット未満・以上で分割
    left = [x for x in lst[1:] if x < pivot]
    right = [x for x in lst[1:] if x >= pivot]

    # 再帰的にソートして結合
    return Qsort(left) + [pivot] + Qsort(right)
print("ソート前:"+str([5,2,6,9,6,1]))
Qresult=Qsort([5,2,6,9,6,1])
print("ソート後:"+str(Qresult))