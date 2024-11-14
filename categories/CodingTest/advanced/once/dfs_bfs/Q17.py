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
    after, get_x, get_y = map(int, input[2].split())
    
    virus_number = deque([i for i in range(1, virus+1)])

    def bfs():
        current_virus = virus_number.popleft()
        for i in range(graph_size):
            for j in range(graph_size):
                if graph[i][j] == current_virus:
                    curr_x = i
                    curr_y = j
                    
                    for i in range(4):
                        nx = curr_x + dx[i]
                        ny = curr_y + dy[i]
                        
                        if nx > 0 and nx < graph_size and ny > 0 and ny < graph_size and graph[nx][ny] == 0:
                            graph[nx][ny] = current_virus
        virus_number.append(current_virus)
        

    for i in range(after):
        bfs()
    print(graph)
    print()

solution(input_1)
solution(input_2)