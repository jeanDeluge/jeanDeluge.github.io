

## preorder
def preorder(nodes, idx): #현재 노드를기준으로 부모노드(0) -> 왼쪽 자식(2n+1 ) -> 오른쪽 자식(2n+2)
    if idx < len(nodes):
        ret = str(nodes[idx])
        ret += preorder(nodes, idx * 2 + 1) 
        ret += preorder(nodes, idx * 2 + 2)
        return ret
    else:
        return ""

## inorder 현재:부모노드  왼쪽자식 -> 부모 지나가기 -> 오른쪽자식  방문
def inorder(nodes, idx):
    if idx < len(nodes):
        # 왼쪽 서브트리 호출
        ret = inorder(nodes, idx * 2 + 1)
        # 현재(부모) 노드 출력 후, 오른쪽 서브 트리 재귀 호출
        ret += str(nodes[idx]) + " "
        ret += inorder(nodes, idx * 2 + 2)
        return ret
    else:
        return ""
## postorder

def postorder(nodes, idx):
    if idx < len(nodes):
        # 왼쪽 -> 오른쪽 -> 부모 순서
        
        ret = postorder(nodes, idx * 2 + 1)
        ret += postorder(nodes, idx * 2 + 2)
        ret += str(nodes[idx]) + " "
        return ret
    else:
        return ""


def solution(nodes):
    return [
        preorder(nodes, 0)[:-1],
        inorder(nodes, 0)[:-1],
        postorder(nodes, 0)[:-1]
    ]


nodes = [1,2,3,4,5,6,7]


print(solution(nodes))







