# 바이러스가 움직이는 것을 기준으로
# 만약 바이러스 상하좌우에서 0 인 걸 발견하면 벽을 세워보고 만약 그 벽의 총 개수가 3을 넘어가면
# 바이러스를 움직이고
# 총 개수가 3이하면 벽을 0에서 1로 만들어본다.
from collections import deque
n, m = map(int, input().split())
graph = []
dx = [ 0, 0, -1, 1]
dy = [ 1, -1, 0, 0]

for _ in range(m):
    given_row = list(map(int, input().split()))
    graph.append(given_row)

queue = deque((0,0))

wall = 3
while queue:
    now = queue.popleft()
    used_wall = 0
    
    if graph[now] == 2:
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if nx < 0 or nx> n or ny < 0 or ny > 0 or map[nx][ny] == 1 or map[nx][ny]==2:
                continue
            else: 
                map[nx][ny] = 1
                used_wall += 1
                
        if used_wall > wall:
            graph.append((nx, ny))
            
            
                    
                
    