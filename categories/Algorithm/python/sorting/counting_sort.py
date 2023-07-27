from typing import MutableSequence

def fsort(a: MutableSequence, max: int) -> None:
    n = len(a) # 정렬할 배열 a 
    f = [0] * (max + 1) # 누적 도수분포표 배열 f
    b = [0] * n # 작업용 배열

    for i in range(n): f[[a[i]]] += 1 # 누적도수분포표에 점수에 해당하는 사람 추가
    for i in range(1, max+1): f[i] +=f[i - 1] # 0점부터 n점까지 학생이 몇명 있는지 누적값으로 만들기

    # a, f를 대조하여서 작업용 배열 b 에 저장한다.

    for i in range(n-1, -1, -1): 
        f[a[i]] -= 1 
        #누적도수분포표의 점수에 해당하는 사람 위치에서 -1을 빼는 이유는 
        #같은 사람이 중복으로 다음 b 의 위치에 가게 하지 않기 위해서
        b[f[a[i]]] = a[i]
    
    #b의 모든 원소를 a에 그대로 복사한다.

    for i in range(n):
        a[i] = b[i]