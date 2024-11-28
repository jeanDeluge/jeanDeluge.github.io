# 경쟁적 전염

# queue로 숫자가 작은 바이러스를 먼저 보내야함
# bfs
from collections import deque

# 움직임
# 상하 좌우

input_1 = ["3 3", ["1 0 2", "0 0 0", "3 0 0"], "2 3 2"]
input_2 = ["3 3", ["1 0 2", "0 0 0", "3 0 0"], "1 2 2"]


dx = [ 0, 0, -1, 1]
dy = [ 1, -1, 0, 0]


def solution(input):
    graph_size, virus = list(map(int, input[0].split()))
    graph = [list(map(int, i.split())) for i in input[1]]
    time, target_x, target_y = map(int, input[2].split())
    
    data = []
    
    for i in range(graph_size):
        for j in range(graph_size):
            if graph[i][j] != 0:
                data.append((graph[i][j],0, i, j)) # 바이러스 종류, 시간, 위치 x, y
                
    data.sort() #낮은번호부터 정렬
    
    q = deque(data)
    
    while q:
        virus, s, x, y = q.popleft()
        if s == time:
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx and nx < graph_size and 0 <= ny and ny < graph_size:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus
                    q.append((virus, s+1, nx, ny))

    print(graph[target_x-1][target_y-1])
        
    
    
                

        
        
        
        
        
    
    

solution(input_1)
solution(input_2)