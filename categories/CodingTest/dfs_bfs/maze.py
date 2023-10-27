size = "5 6"
maze = "101010 111111 000001 111111 111111"

# 방법: 내 위치의 다음번 위치에 내가 몇 번째로 도착했는지 적기

def solution(size, maze):
    n,m = map(int, size.split())
    rows = maze.split()
    
    maze_map = []
    for row in rows:
        maze_map.append(list(map(int, row)))
    
    print(maze_map)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    stack = [(0, 0)]
    
    while stack:
        x, y = stack.pop()
        if maze_map[x][y] > 0 :
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maze_map[nx][ny] == 0:
                    continue
                if maze_map[nx][ny] == 1:
                    maze_map[nx][ny] = maze_map[x][y] + 1
                    stack.append((nx, ny))
    print(maze_map)
    return maze_map[n-1][m-1]

print(solution(size, maze))