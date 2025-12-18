def quick_sort(arr):
    # 要素数が1以下ならそのまま返す
    if len(arr) <= 1:
        return arr

    # 基準値（pivot）を選ぶ（ここでは先頭）
    pivot = arr[0]

    # pivotより小さい要素
    left = [x for x in arr[1:] if x <= pivot]

    # pivotより大きい要素
    right = [x for x in arr[1:] if x > pivot]

    # 再帰的にソート
    return quick_sort(left) + [pivot] + quick_sort(right)


# 動作確認用（提出時に消してもOK）
if __name__ == "__main__":
    data = [5, 3, 8, 4, 2, 7, 1, 6]
    print("before:", data)
    print("after :", quick_sort(data))
