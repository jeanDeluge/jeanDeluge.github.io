size = "4 5"
frame = "00110 00011 11111 00000"

def solution(size, frame):
    result = 0
    n, m = map(int, size.split())
    graph = []
    rows = frame.split()
    
    for row in rows:
        graph.append([int(char) for char in row])
        
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                result += 1
                stack = [(i,j)]
                print(stack)
                while stack:
                    x, y = stack.pop()
                    
                    if graph[x][y] == 0:
                        graph[x][y] = 1
                        if x > 0:
                            stack.append((x - 1, y))
                        if x < n - 1:
                            stack.append((x + 1, y))
                        if y > 0:
                            stack.append((x, y - 1))
                        if y < m - 1:
                            stack.append((x, y + 1))
                        print(stack)
    return result
result = solution(size, frame)

print(result)