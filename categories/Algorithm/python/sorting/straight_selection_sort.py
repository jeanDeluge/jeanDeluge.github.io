# 배열이 된 부분과 안된 부분 나누기
# 배열이 안된 부분에서 제일 작은값 뽑고
# 배열이 된 부분 다음 번과 교환하기
from typing import MutableSequence

def sort(a):
    n = len(a)

    for i in range(n):
        m = i # 제일 작은 부분
        ## i 가 증가할 수 록 배열 앞쪽이 정렬됨 
        for j in range(i+1, n):
            if a[i] < a[m]:
                m = i
        a[i], a[m] = a[m], a[i]

