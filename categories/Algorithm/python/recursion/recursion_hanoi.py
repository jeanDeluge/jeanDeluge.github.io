def hanoi(n:int, start = 1, destination = 3, temp = 2): 
    if n <= 1:
        print(f'원반[{n}] 을 {start}에서 {destination}으로 옮겼습니다.')
        return

    hanoi(n-1, start, temp, destination)#1~n-1 번째는 기둥 2로 옮겨야함 
    print(f'원반[{n}] 을 {start}에서 {destination}으로 옮겼습니다.')
    # n-1  번째까지 원반을 다시 원반을 기둥2에서 기둥3으로 옮겨야함
    hanoi(n-1, temp, destination, start)

n = int(input())
print(hanoi(n))