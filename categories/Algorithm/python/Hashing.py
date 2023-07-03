# 오픈주소법으로 해싱
from typing import Any
import hashlib

# Node 개별 버킷을 의미
class Node: 

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key # 키
        self.value = value # 값
        self.next = next # 뒤쪽 노드 참조

# ChainedHash 클래스 만들기 -> 해시 테이블 만들기
# field
# - capacity : 해시테이블의 크기
# - table: 해시 테이블을 저장하는 list 형식의 배열 
# -> 해시테이블 크기 만큼의 버킷의 리스트
# hash_value() 해시값을 생성하는 해시함수 생성
# 정의 : 키 값을 해시값으로 변환해주는 함수

class ChaindHash:
    def __init__(self, capacity : Any ) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity
    
    def hash_value(self, key: Any) -> int :
        # key:value -> hash - key :value
        # 키 값이 만약에 정수라면
        if isinstance(key, int):
            return key % self.capacity
        # 키 값이 만약 정수가 아니라면
        # 문자열을 인코딩해서 해시값을 16진수 문자열로 만든다.
        # 만든 16진수 문자열을 정수형으로 바꿔서 그것을 self.capacity로 나눈다.
        return (int(hashlib.sha512(str(key).encode()).hexdigest(), 16) % self.capacity)
    
    ## search 함수
    ## key 값의 해시값을 구하기
    ## 해당 해시값에 해당하는 노드 리스트를 가지고 오기
    ## 노드들을 탐색해서 해당 키를 찾기
    ## 키를 찾으면 해당 값을 반환해주기
    ## 못찾았으면 None 반환

    def search(self, key: Any) -> Any:
        hash = self.hash_value(key) # 해당 키의 해시값찾기
        #키의 해시값에 맞는 노드 리스트 가져오기
        curr_node = self.table[hash] # 버킷 중에허 가장 첫번째 노드가져옴

        # 노드에 딸린 리스트안을 탐색 만약 None이면 탐색을 종료하고 
        while curr_node is not None:
            if curr_node.key == key:
                return curr_node.value
            curr_node = curr_node.next
        
        return None

    def add(self, key: Any, value: Any) -> bool:
        # hash 값 만들기
        # 해당 해시 위치 노드 가져오기

        hash = self.hash_value(key)
        curr_node = self.table[hash] ## 버킷 중에서 가장 첫번째 노드 가져옴

        # 노드에 해당 키가 있다면 추가 실패
        while curr_node is not None:
            if curr_node.key == key: 
                return False
            curr_node = curr_node.next
        
        # 버킷 내부 리스트를 다 뒤져도 해당 키가 없다면 노드를 만들어서
        # 노드 뒤에다가 첫번째 노드 붙여넣기
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True
        
    ## remove 함수
    #키를 hash 값으로 만들어서 해당 키를 찾기
    #선형 검색하기
    #키가 없다면 false
    #키가 있다면 그 노드에서 삭제
    # 이때, 노드를 삭제 할 때 맨 뒷부분 이면 맨 뒤에 만 삭제하면됨
    # 맨 앞 부분이면, 버킷의 첫 노드를 두번째로 바꿔주고
    #  두번째~ n-1 번째면 삭제 후, k 번째 기준으로 k-1의 뒤에 k+1 번째 뒤부터의 리스트를 붙여줘야함

    def remove(self, key) -> bool:
        hash = self.hash_value(key)
        curr_node = self.table[hash]
        previous_node = None

        while curr_node is not None:
            if curr_node[key] == key:
                if previous_node is None:
                    self.table[hash] = curr_node.next
                else:
                    previous_node.next = curr_node.next
                previous_node = curr_node
                curr_node = curr_node.next
            return False
    
    ## 모든 원소 출력

    def dump(self) -> None:

        for i in range(self.capacity):
            curr_node = self.table[i]
            print(i, end ="")
            while curr_node is not None:
                print(f' -> {curr_node.key} ({curr_node.value})', end="")
                curr_node = curr_node.next
            print()
