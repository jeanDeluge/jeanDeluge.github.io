# 버블 정렬 - 단순교환정렬

이웃한 두 원소의 대소관계를 비교하여 필요에 따라 교환 반복

- 패스 pass : 비교하고 교환하는 과정

## 세이커 정렬 Shaker sort 

버블 정렬을 오름차순으로 뒤에서 부터 패스하도록 만들었을때,
만약 9 1 2 3 4 5 의 경우에 뒤에서 부터 확인해야하니 비효율적.
그러므로 패스 스캔 방향을 번갈아 바꾸는 것이 좋다.