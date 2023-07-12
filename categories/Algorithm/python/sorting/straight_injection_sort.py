
# 리스트에서 앞에서 부터 원소를 선택
# i 가 증가할 수록 정렬된 원소가 증가함
# 정렬되지 않은 쪽 맨 앞에 있는 원소를 주목한 후,
# 정렬된 부분에서 크기를 비교하여 알맞은 위치에 넣기


from typing import MutableSequence

def injection(a: MutableSequence) -> None:
    
    n = len(a)

    for i in range(n):
        j = i
        # 정렬 하고자 하는 원소 주목
        target = a[j]
        while j > 0 and a[j - 1] > target:
            a[j] = a[j-1] # 앞의 원소를 현재 원소에 대입해서 바꿔버리기
            j -= 1 #계속 tmp 보다 작을 때까지 수행하도록 앞으로 보냄
        # 앞에 다 보내고 나면 마지막에 타겟보다 작은 경우에 그 작은 부분 다음에 타겟을 넣음
        a[j] = target

if __name__ == "__main__":
    a = [ 1, 3, 5, 6, 4, 2]

    injection(a)
    print(a)
