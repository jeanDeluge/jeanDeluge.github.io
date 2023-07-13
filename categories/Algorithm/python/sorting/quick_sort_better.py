# 피벗을 선택하도록 함
# 원소 그룹 안의 갯수가 9개 이하이면 단순 삽입 정렬 실행

from typing import MutableSequence

# 피벗 정하기
def sort3(a: MutableSequence, left: int, mid: int, right: int) -> None:
    # 맨 왼쪽, 가운데, 맨 오른쪽을  오름차순으로 정리하기
    # [4, 3, 1]
    if a[left] < a[mid] : a[left], a[mid] = a[mid] , a[left]
    if a[mid] > a[right] : a[mid], a[right] = a[right], a[mid]
    # 여기서 한번더 만약 [4, 1, 3] 이 되어서 가작 작은 수가 가운데 오는 걸 방지
    if a[mid] < a[left] : a[left], a[mid] = a[mid] , a[left]
    return mid

def insert_sort(a: MutableSequence, left:int, right:int) -> None:
    for i in range(left+1, right+1):
        j = i 
        tmp = a[i]
        while j > 0 and a[j -1] > tmp: 
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

def qsort(a:MutableSequence, left:int, right:int) -> None:

    if right - left < 9:
        insert_sort(a, left, right)
    else:
        # 피벗 정하기
        pl = left
        pr = right
        mid = sort3(a, pl, (pl+pr)//2 ,pr)
        pivot = a[mid]
 
        #중간 값과 끝에서 두번째 값이랑 바꾸기
        a[mid], a[pr - 1] = a[pr- 1] , a[mid]
        # pl 위치 변경 # 피벗 정한 것 중에 가장 왼쪽 값은 비교했으니까 오른쪽으로 한칸 옮김
        pl += 1
        # pr 위치 변경 # 피벗 다음이 어야함
        pr -= 2
        while pl <= pr:
            while a[pl] < pivot : pl += 1
            while a[pr] > pivot : pr -= 1
            if pl <= pr:
                a[pl] , a[pr] = a[pr] , a[pl]
                pl += 1
                pr -= 1

        if left < pivot:
            qsort(a, left, pr)
        if right > pivot:
            qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    qsort(a, 0, len(a) - 1)

if __name__ == "__main__":
    a = [ 1, 3, 5, 6, 4, 2, 1, 3, 9, 8, 10, 15, 13, 12, 11, 14]
    quick_sort(a)
    print(a)