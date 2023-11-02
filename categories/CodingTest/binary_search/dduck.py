def give_dduck():
    # 4 6 떡의 갯수 요청한 떡의 길이
    # 19 15 10 17 떡 길이
    
    num, length = map(int, input().split())
    dduck = map(int, input().split())
    
    start = 0
    end = max(dduck)
    
    result = 0
    
    while(start <= end):
        total = 0
        mid = (start + end)//2
        
        for cut in dduck:
            if cut > mid:
                total += cud - mid
                
        if total < m:
            end = mid - 1
        
        else:
            result = mids
            start = mid + 1
        