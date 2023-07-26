from typing import MutableSequence

def heap_sort(a: MutableSequence):

    def down_heap(a:MutableSequence, left: int, right: int): # 힙으로 만들기
        #a[left] ~ a[right] 배열에서 힙정렬
        temp = a[left] # 일단 맨 앞의 값을 가져옴 # 루트임

        parent = left # 현재 루트는 parent 이므로
        
        while parent < (right + 1) // 2: # parent 가 자기 자식의 위치보다 높은 위치에 있을대까지
            cl = parent * 2 + 1 # 왼쪽 자식 
            cr = cl + 1 # 오른쪽 자식

            child = cr if cr <= right and a[cr] > a[cl] else cl 
            # 왼쪽, 오른쪽 자식 중에 큰 쪽의 인덱스가 child 위치임
            if temp >= a[child]: # 루트의 값이 child 위치의 원소 보다 크면 멈추고 parent 인덱스 위치의 a 배열 원소에 맨 앞을 값을 넣기
                break
            a[parent] = a[child] # 루트의 값이 child위치의 원소보다 작으면 루트위치에 루트보다 큰 차일드를 놓고
            parent = child # 루트의 인덱스를 차일드 인덱스로 변환
        a[parent] = temp 
        # 루트의 값이 child 위치의 원소보다 컸을때 , 자기 자식의 위치보다 낮은 위치에 있다면 루트값을 부모자리에 넣어줌
    
    n = len(a)

    for i in range((n-1)//2, -1, -1): 
        down_heap(a, i, n-1) # 힙으로 만들기

    for i in range(n-1, 0, -1): # 최댓값인 a[0]와 마지막원소를 교환 후
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i-1) # 힙으로 만들기

