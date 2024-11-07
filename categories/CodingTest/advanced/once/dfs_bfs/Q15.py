from collections import deque 


n, m, k, x = map(int, input().split())
roots = [[] for _ in range(n+1)]
distance = [-1] * (n+1)
distance[x] = 0


for _ in range(m):
    a, b = map(int, input().split())
    roots[a].append(b)
    
queue = deque([x])

while queue:
    curr = queue.popleft()
    for next in roots[curr]:
        if distance[next] == -1:
            distance[next] = distance[curr] + 1
            queue.append(next)
        
    
check = False
for i in range(len(distance)):
    if distance[i] == k:
        print(i)
    else:
        check = True
        
if check is False:
    print(-1)