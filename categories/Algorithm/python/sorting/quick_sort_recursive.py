from typing import MutableSequence

def quick(a: MutableSequence, left:int, right: int) -> None:

    pl = left
    pr = right
    x = a[ (left + right)// 2]


    while pl <= pr:
            # a[pl] 이 x 피벗 큰 경우를 찾는다.
            while a[pl] < x : pl += 1
            # a[pr] 이 x 피벗보다 작은 경우를 찾는다.
            while a[pr] > x : pr -= 1
            # 그 두 경우를 찾았을때, 
            # pl <= pr 일 경우만 서로 교환해준다.
            if pl <= pr:
                a[pl], a[pr] = a[pr] , a[pl]
                pl += 1
                pr -= 1
    # 서로 다 교환이 끝나면
    # 현재 pr 이 계속 left 보다 큰 상태이면 left - pr 까지 그룹을 퀵정렬
    if left < pr : quick(a, left, pr)
    # 소팅이 끝난시점에서 pl 이 right 보다 작은 경우 pl - right까지의 그룹을 퀵 정렬
    if pl < right : quick(a, pl, right)


if __name__ == "__main__":
    a = [ 1, 3, 5, 6, 4, 2, 1, 3, 9, 8, 10, 15, 13, 12, 11, 14]

    quick(a, 0, len(a)-1)
    print(a)