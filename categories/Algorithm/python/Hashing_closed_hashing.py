## 가능한 빈 곳으로 재해싱하기

## 원소 추가
# 빈 해시값이 나타날 때까지 재해싱하기

## 원소 삭제
## 첫 해싱에서 첫 해시값에 해당하는 원소가 삭제되어있다면, 해당 원소가 이미 삭제되고 없다고 나올 것
## 그것을 방지하기 위해서는 삭제했던 해시값은 따로 표기가 필요하고,
## 표기가 있다면, 재해싱해서 바른 해싱값을 찾아갈 수 있어야함
## 원소 검색
## 첫 해싱에서 첫 해시값을 받았을때 애초부터 비어있었으면 실패
## 첫 해싱에서 삭제되어있덨던 해시면 다시 재해싱해서 값을 비교하기
## 


from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# Bucket 비었는지, 삭제되어있는지, 채워져있는지 확인해야함
class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2

# 해시를 구성하는 버킷 클래스 구현
class Bucket:
    # 초기화
    def __init__(self, key: Any = None, value: Any = None, 
                    stat: Status = Status.Empty ) -> None:
        self.key = key
        self.value = value
        self.stat = stat
    
    # 값 넣기
    def set(self, key: Any, value: Any, stat: Status ) -> None:
        self.key = key
        self.value = value
        self.stat = stat

    def set_status(self, stat: Status) -> None:
        self.stat = stat

# 오픈 주소법으로 해시클래스 구현

class ClosedHash:

    ## 초기화 , 해시테이블 만들어주기

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity

    # 해시함수 만들기
    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity)
    
    # 재 해시
    def rehash_value(self, key: Any) -> int:
        return (self.hash_value(key) + 1 ) % self.capacity # 한칸 옮기기
    
    
    ## 찾기
    ### 해당키 버킷찾기
    def search_bucket(self, key: Any):
        hash = self.hash_value(key)
        bucket = self.table[hash]

        # 해당 버킷의 상태가 
        # empty면 원래 없는거니까 break
        # occupied 면 해당 되는 거니까 return bucket 
        # delete 면 재해싱해야함 -> 전체적으로 for 문사용

        for _ in range(self.capacity):
            if bucket.stat == Status.EMPTY:
                break
            elif bucket.stat == Status.OCCUPIED:
                return bucket
            else:
                hash = self.rehash_value(hash)
                bucket = self.table[hash]
        
        return None
    

    ### 키의 값 반환하기

    def search(self, key: Any):
        # 버킷을 찾아서 거기서 값을 돌려받음
        bucket = self.search_bucket()

        # 일단 None 이 아니면 버킷을 반환했다는 것
        if bucket is not None:
            return bucket.value
        else:
            return None

    ## 추가

    def add(self, key: Any, value: Any) -> bool:

        # 만약 key에 해당하는 해시에서 키-값이 있다면 False : 이미 존재하는 키값임
        if self.search(key) is not None:
            return False
        

        # 만약 key에 해당하는 해시의 버킷의 상태가 비어있거나, 삭제되어있다면 추가
        # 아니면 재해시 -> 전체적으로 for 문
        hash = self.hash_value(key)
        bucket = self.table[hash]
        for _ in range(self.capacity):
            if bucket.stat == Status.EMPTY or bucket.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            bucket = self.table[hash]


        # 재해시를 해도 못집어넣었으면 False. 테이블 꽉참
        return False
    
    ## 삭제

    def delete(self, key:Any) -> bool:
        # 만약 key 에 해당하는 해시값의 버킷이 empty, delete 여서 찾아도 None 이면 삭제 실패
        # 애초에 값이 없으므로

        bucket = self.search_bucket(key)

        if bucket is None:
            return False
        bucket.set_status(Status.DELETED)
        return True

        # 만약 None 이 아니라면 값이 있는 것이므로
        # 해당 버킷 상태를 delete로 바꿔둠

    ## 덤프

    def dump(self) -> None:
        for i in range(self.capacity):
            print(f'{i:2} ', end='') # 2칸 숫자로 줌 왼쪽부터 채우기
            if self.table[i].stat == Status.EMPTY:
                print("--미등록---")
            elif self.table[i].stat == Status.DELETED:
                print("--삭제됨--")
            elif self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')

