# 인구 이동 

# 국경산 공유하는 두나라 인구 차이가 L 명 이상 R 명이하, 두 나라 공유 국경선 열기
# 열어야 하는 국경선이 모두 열리면 인구 이동
# 국경선 열려 있으면 열린 국경선 인접 나라끼리 연합
# 연합 이르구 있는 각 칸의 인구수는 연합인구수 / 연합수 => 소수점 버리기
# 연합 해체, 모든 국경선 닫기

# 인구 이동이 몇번 일어나는지

# N L R  땅크기, 범위(0 < L < R < 100)
# 나라당 인구수

from collections import deque

input_1 = ["2 40 50", ["50 30", "20 40"]]
input_2 = ["2 20 50", ["50 30", "30 40"]]
def solution(given_input):
    # 맵 만들기
    
    N, L, R = map(int, given_input[0].split())
    
    ground = [list(map(int, given_input[1][i].split()) )for i in range(N)]
    
    dx = [0, 0 , -1, 1]
    dy = [1, -1 , 0, 0]
    
    
    def united(current,index):
        unite = []
        unite.append(current)
        
        x,y = current
        q = deque()
        
        q.append(current)
        
        total_popularation = ground[x][y]
        number_of_unite = 1
        
        
        while q:
            x,y = q.popleft()
            
            current_population = ground[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < N and 0 <= ny  < N and union[nx][ny] == -1:
                    
                    differ = abs(ground[nx][ny] -  current_population)
                
                    if L <= differ <= R:
                        q.append((nx, ny))
                        unite.append((nx, ny))
                        union[nx][ny] = index
                        number_of_unite += 1
                        total_popularation += ground[nx][ny]


        for i, j in unite:
            ground[i][j] = total_popularation // number_of_unite

        return number_of_unite
    opened_count = 0
    
    # 한번 연합 다 찾고 다시 찾기
    while True:
        union = [ [-1] * N for _ in range(N)]
        index = 0
        for i in range(N):
            for j in range(N):
                if union[i][j] == -1 :
                    united((i,j),index)
                    index += 1
        
        
        if index == N * N:
            break
        opened_count += 1

    return opened_count
    

print(solution(input_1))
print(solution(input_2))
