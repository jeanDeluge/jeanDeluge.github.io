# 감시피하기
# 선생님 범위 선생님 위치 + 상하좌우 끝까지 
# 단, 장애물 뒤에있는 학생은 못봄
# 장애물 3개 설치해서 모든 학생이 감시 피할 수 있으면 

# 출력은 YES, 아니면 NO



def solution(given_input):
    n = given_input[0]
    given_graph = given_input[1]
    

    graph = []
    
    dx = [ 0, 0, -1, 1]
    dy = [ 1, -1, 0, 0]
    
    # 맵 구성
    
    for i in range(n):
        row =list(map(str, given_graph[i].split()))
        graph.append(row)
    
    def is_safe(): 
        for x in range(n):
            for y in range(n):
                if graph[x][y] == 'T':
                    if can_see(x,y):
                        return False
                    
        return True

                
    def can_see(x,y):
        for i in range(4):
            while True:
                x += dx[i]
                y += dy[i]
                if x < n and x > 0 and y > 0 and y < n and graph[x][y] == 'S':
                    return True
                break
            return False
        
        
                    
    def dfs(count):
        if count == 3:
            return is_safe()
    
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X': # 백트래킹 -> 이해는 못했지만, 바이러스 막는 기능 Q16번과 유사
                    graph[i][j] == 'O'
                    if dfs(count+1):
                        return True
                    graph[i][j] == 'X'
        return False
    
    if dfs(0):
        return "YES"
    else:
        return "NO"

input_1 = (5, [
    'X S X X T',
    'T X S X X',
    'X X X X X',
    'X T X X X',
    'X X T X X'
])

input_2 = (4, [
    'S S S T',
    'X X X X',
    'X X X X',
    'T T T X'
])

print(solution(input_1))