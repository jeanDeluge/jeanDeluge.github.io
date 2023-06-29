# pl : 맨처음, pc: 중간 , pr : 마지막 인덱스
# key < pc 이면
# pr = pc-1
# key > pc이면
# pl = pc + 1

# 검색 종료 조건
# 키 일치
# pr = pl 인 경우 탐색 끝냈을때

# 시간 복잡도 : logN , 이유는 계속 1/2 씩 검색 횟수가 줄어들어서.
#   검색 성공시 : log(N-1), 하나 탐색한 중간에 빠져나와서
#   검색 실패시 : log(N+1) (1 은 pr, pl 이 서로 위치 바뀌는 것까지)
# 공간 복잡도 :

from typing import Any, Sequence

def binary_search(a: Sequence, key: Any ):
    pr = len(a) -1 
    pl = 0

    while True:
        pc = (pl + pr )//2

        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pr = pc - 1
        else:
            pl = pc + 1

        if pr < pl:
            break

    return -1
