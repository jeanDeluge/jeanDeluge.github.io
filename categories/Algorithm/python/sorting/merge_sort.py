from typing import Sequence, MutableSequence



def merge_sort(a: MutableSequence) -> None:    

    if len(a) <= 1:
        return a
    
    mid = len(a) // 2
    # 분할

    left_list = merge_sort(a[mid:])
    right_list = merge_sort(a[:mid])

    return merge(left_list, right_list)

def merge(left, right):
    buff = []
    na = len(left)
    nb = len(right)
    pointer_a = pointer_b = 0

    # 두 리스트를 비교했을 때 각 포인터의 위치의 값이 더 작은 쪽을 buff에 넣기
    while pointer_a < na and pointer_b < nb:
        if left[pointer_a] < right[pointer_b]:
            buff.append(left[pointer_a])
            pointer_a += 1

        else:
            buff.append(right[pointer_b])
            pointer_b += 1
        
    # 두 리스트 남은거 buff에 넣기

    if pointer_a < na:
        buff += left[pointer_a:]
    
    if pointer_b < na:
        buff += right[pointer_b:]

    print(buff)
    return buff




if __name__ == "__main__":
    a = [ 1, 3, 5, 6, 4, 2, 1, 3, 9, 8, 10, 15, 13, 12, 11, 14]
    merge_sort(a)
