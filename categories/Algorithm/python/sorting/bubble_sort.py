from typing import MutableSequence

# 단방향 버블 소트

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)

    for i in range(n):
        exchange = 0 # 패스에서 교환횟수
        ## i번째까지 뒤에서부터 탐색이 필요
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                ## 만약 현재 인덱스보다 이전 인덱스가 크다면 서로 바꿔줘서, 현재의 것을 뒤로 보내야함
                a[j-1], a[j] = a[j], a[j-1]
                print(a)




# 개선 1 : 서로 비교하다가, i번째와 i-1 번째가 서로 비교했을대, 바꿀 필요가 없다고 판단되면
# 1~i-1 번째는 이미 정렬이 되어있는 것
# 앞쪽으로 더이상 비교할 필요가 없으니 
# 스캔 범위를 제한 해야함

def better_bubble_sort(a: MutableSequence) -> None:

    n = len(a)
    # 어디까지 탐색해야하는지 포인터가 필요함
    k = 0

    # 만약 포인터가 n-1 번째와 같아지면 서로 비교할 필요가 여기서 부터 없어짐
    while k < n-1:
        # 일단 맨 뒤에 포인터를 가져감
        last = n - 1
        for j in range(n-1, k, -1):
            if a[j-1] > a[j]: # 만약 서로 바꿀 수 있다면 바꿔야하고
                a[j-1], a[j] = a[j], a[j-1]
                #현재 포인터 바꿀 필요없는 부분을 가르키도록함
                last = j # 이미 바꾸었으니 j번째는 바꿀 필요없다고 알려줘야함
        # 다음 반복에 현재 포인터 전달
        k = last

# 셰이커 정렬 : 

def shaker(a: MutableSequence) -> None:

    left = 0
    right = len(a) - 1
    last = right

    while left < right :
        # left = right 가 같은 순간이 오면 정렬을 끝내야함
        # 먼저 left 위치 조절. 
        # 뒤에서 맨 앞으로 스캔하여 정렬을 하고, 정렬을 끝내면 더이상 정렬이 필요없는 그 순번의 원소 인덱스를 가져와야함
        for j in range(right, left , -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        left = last

        for j in range(left, right):
        # 앞에서 뒤로 스캔하여 정렬을 하고, 정렬을 끝내면 더이상 정렬이 필요없는 그 순번의 인덱스를 가져옴
            if a[j] > a[j+1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last


# 셰이커 
if __name__ == "__main__":
    
    a = [1, 4, 5, 3, 6, 2]

    shaker(a)

    print(a)



