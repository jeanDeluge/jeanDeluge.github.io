example_1 = [[7, 7] , ["2 0 0 0 1 1 0", "0 0 1 0 1 2 0", "0 1 1 0 1 0 0", "0 1 0 0 0 0 0", "0 0 0 0 0 1 1", "0 1 0 0 0 0 0", "0 1 0 0 0 0 0"], ]
example_2 = [[4, 6], [ " 0 0 0 0 0 0", "1 0 0 0 0 2", "1 1 1 0 0 2", "0 0 0 0 0 2"]]
# 바이러스가 퍼지도록 하고,
# 벽을 두면서 탐색
# 벽을 설치하는 dfs
# 벽을 설치를 다 했으면
# 바이러스는 있는 기준으로 모두 퍼져나가고
# 벽을 고정시키고
# 남은 0을 갯수 탐색

# 벽을 설치를 다 못했으면
# 미리 한번 1개 설치해보고
# 그 다음에서 다음 상황을 한번 보고
# 다시 벽을 철거한다.
def solution(example):
    n, m = example[0]
    graph = [ list(map(int, i.split())) for i in example[1] ]
    temp = [[0] * m for _ in range(n)]

    result = 0 
    
    def virus(x,y):
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < n and ny>= 0 and ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    virus(nx, ny)
                       
    def get_safe_area():
        area = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    area += 1
        return area    
    
    def dfs(count):
        nonlocal result
        if count == 3:
            for i in range(n):
                for j in range(m):
                    temp[i][j] = graph[i][j]
                
            for i in range(n):
                for j in range(m):
                    if temp[i][j] == 2:
                        virus(i, j)
            result = max(result, get_safe_area())
            return

        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    count += 1
                    dfs(count)
                    graph[i][j] = 0
                    count -= 1
                    
    dfs(0)       
    print(result)
solution(example_1)