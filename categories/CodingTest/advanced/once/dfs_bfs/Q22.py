from collections import deque
def solution(board):
    
    n = len(board)
    n_board = [ [1] * (n + 2) for _ in range(n + 2)]
    
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                n_board[i+1][j+1] = 0
                
    q = deque()
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
            
    visited=set()
    
    
    start = ((1,1),(1,2))
    
    # 다음 움직임이 가능한 자리 넣기
    q = deque([])
    q.append((start, 0))
    
    visited.add(start)
    
    
    while q:
        
        (pos1, pos2), time = q.popleft()
        x1, y1 = pos1
        x2, y2 = pos2
        
        if (x1 == n and y1 == n) or (x2 ==n and y2 ==n):
            return time
        
        for i in range(4):
            new_pos1 = (x1+dx[i], y1+dy[i])
            new_pos2 = (x2+dx[i], y2+dy[i])
            
            if n_board[new_pos1[0]][new_pos1[1]] == 0 and n_board[new_pos2[0]][[new_pos2[1]]] == 0:
                
                if (new_pos1, new_pos2) not in visited:
                    visited.add((new_pos1, new_pos2))
                    q.append(((new_pos1, new_pos2), time+1))
                    
            if x1 == x2:
                for i in [-1, 1]:
                    if n_board[x1+i][y1] == 0 and n_board[x2+i][y2] == 0:
                        new_pos1 = (x1+i, y1)
                        new_pos2 = (x2+i, y2)
                        
                        if (new_pos1, pos1) not in visited:
                            visited.add((new_pos1, pos1))
                            q.append(((new_pos1, pos1), time+1))
                        if (new_pos2, pos2) not in visited:
                            visited.add((new_pos1, pos1))
                            q.append(((new_pos1, pos1), time+1))
                            
            if y1 == y2:
                for i in [-1, 1]:
                    if n_board[x1][y1+i] == 0 and n_board[x2][y2+i] == 0:
                        new_pos1 = (x1, y1+i)
                        new_pos2 = (x2, y2+i)
                        
                        if (new_pos1, pos1) not in visited:
                            visited.add((new_pos1, pos1))
                            q.append(((new_pos1, pos1), time+1))
                        if (new_pos2, pos2) not in visited:
                            visited.add((new_pos2, pos2))
                            q.append(((new_pos2, pos2), time+1))

    return 0
    