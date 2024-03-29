# 셸 정렬

단순 삽입 정렬의 장점은 살리고 단점은 보완
먼저 정렬할 배열의 원소를 그룹으로 나눠 각 그룹별로 정렬 수행



## 단순 삽입 정렬의 장/단점
장점: 정렬이 거의 되어있을때는 O(n)으로 빠르고, 
단점: 역순으로 정렬된 상태에서은 O(n^2)이다., 원소가 많으면 많을 수록 효율이 떨어진다.


## 셀 정렬 과정
정렬할 때 그룹으로 나눠서 정렬한다
이 때 나누는 그룹은 h칸 떨어진 원소끼리 그룹을 짜고 서로 교환한다.
예를 들면 8칸씩 떨어진 원소끼리 그룹을 묶어 정렬을 수행할 때를 h-정렬이라고 한다.

## h-정렬 시에 h의 선택
h값이 서로 배수가 될 경우 예를 들면,
원소의 개수가 8 이고, [8, 3, 2, 4, 1, 7, 5, 6] 일때,
4-정렬 시 그룹은 [8, 1], [3, 7], [2, 5] , [4, 6]
이고 정렬 결과는 
[1, 3, 2, 4, 8, 7, 5, 6]
2-정렬 시 그룹은 
[1, 2, 8, 5], [3, 4, 7, 6] 으로,
[8, 1] 과 [2, 5]과 그대로 같은 그룹에 있는 것을 알수있다.
그래서 서로 셔플되지 못하므로 정렬의 의미가 없어짐

그래서 h 값이 배수가 되지 않게 해야함

## 불안정정렬

서로 이웃하는게 아닌 멀리 떨어진 것 끼리 교환하기 때문에 중복인 값이 원래 있던 순서대로 정렬되지는 않음.