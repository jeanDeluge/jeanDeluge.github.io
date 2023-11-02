def binary(array, target, start, end):
    while start <= end:
        mid = (start + end) //2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
        
        return None

def find_parts():
    # 5 가게 부품 갯수
    # 8 3 7 9 2
    # 3 요청부품 갯수
    # 5 7 9 요청한 부품 종류
    
    # 이진 탐색을 요청 부품갯수 만큼 돌린다.
    # 정렬을 하게 되면 
    
    
    shop_stock = int(input())
    stop_stock_parts = map(int, input().split())
    
    request_nums = int(input())
    request_parts_nums = map(int, input().split()) 
    
    for part in requst_parts_nums:
        result = binary(stop_stock_parts, part, 0, n-1)
        
        if result != None:
            print("yes", end=" ")
        else:
            print("no", end=" ")
    