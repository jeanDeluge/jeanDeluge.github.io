# 단순 삽입 정렬과 비슷,
# h 값으로 그룹화해야함
from typing import MutableSequence

# 종료 조건
# h값이 1 이하 일때


def shell_sort(a: MutableSequence) -> None:
    
    n = len(a)
    h = 1

    # h의 최댓값 찾기, 초기 값이 지나치게 크지 않도록 함
    while(h < n//9): # n을 9로 나누었을 때의 몫보다 작을 때까지
        h = h * 3 + 1
        
    while(h > 0):
        # h번째에서 n번째까지만 탐색 맨 앞의 i-h 번째는 나중에 지정할 것이고, 그 다음 부터는 n 안에서 h 만큼 띄어서 비교
        for i in range(h, n):
            j = i - h # 만약 h가 가장 큰 수 일 때면, 맨 첫 번째 a[j]
            tmp = a[i] # h가 가장 큰 수일 때 두번째임  
            while j > 0 and a[j] > tmp: # 첫번째가 더 클때까지. 첫번째 것이 작아지면 정렬이 완료된 것
                a[j+h] = a[j] # h번째에 맨 첫번째 수 주입
                j -= h # 다음 회차에서 다음 번째 를 탐색하도록 바꿈
                print(j, a[j+h], a[j])
            a[j+h] = tmp # 모든 탐색이 끝나고, h그룹의 마지막번째에 tmp 삽입
            
        h //= 3


if __name__ == "__main__":
    a = [ 1, 3, 5, 6, 4, 2, 1, 3, 9, 8, 10, 15, 13, 12, 11, 14]

    shell_sort(a)
    print(a)