class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key
        
class BST:
    
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            curr = self.root
            while True: 
                # 삽입하려는 값(key) 이 현재노드 보다 작으면 왼쪽 자식 노드로 이동
                if key < curr.val:
                    if curr.left: # 만약 현재 노드에게 왼쪽 노드가 있다면
                        curr = curr.left # 현재 노드 값을 왼쪽 자식노드에 대입하기
                    else: # 만약 현재 노드에게 왼쪽 노드가 없고, 삽입하려는 값이 현재 노드보다 작으면 현재 노드 왼쪽에 노드를 만들어주기
                        curr.left = Node(key)
                        break # 왼쪽 노드를 만들어주고 삽입 종료 = 이유는 더이상 넣을 자식 노드가 없으므로
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(key) # 객체넣기
                        break
    def search(self, key): ## key = 찾으려고 하는 값
        curr = self.root # 루트부터 찾기
        # 현재 노드가 존재하고 찾으려는 값과 현재 노드가 일치 하지 않으면  계속 찾기
        while curr and curr.val != key:
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr
    
    
def solution(lst, search_lst):
    bst = BST()
    
    for key in lst:
        bst.insert(key)
    result = []
    
    for search_val in search_lst:
        if bst.search(search_val):
            result.append(True)
        else:
            result.append(False)
    return result

print(solution([5,3,8,4,2,1,7,10], [1,2,5,6]))
            
                        
                        

lst = [5, 3, 8, 4, 2, 1, 7, 10]