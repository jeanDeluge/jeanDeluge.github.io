# 파이썬 라이브러리

1. bisect 라이브러리
bisect.bisect_left(right) 는 해당 **정렬된** 리스트에서 타겟값을 넣을 때의 위치를 알려준다.

left는 타겟값을 넣을 곳,
right는 타겟값을 넣을 위치 + 1 의 인덱스를 가르켜줌
```
import bisect

a = [1, 2, 2, 3, 4, 5]
target = 2

b = bisect.bisect_left(a,target) # 1
c = bisect.bisect_right(a, target) # 3

```