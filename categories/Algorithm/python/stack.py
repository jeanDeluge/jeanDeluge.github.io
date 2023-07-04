from typing import Any

class FixedStack:
    # 고정 길이 스택 

    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stack = [None] * capacity
        self.capacity = capacity
        self.pointer = 0

    def __len__(self) -> int:
        return self.pointer
    
    def push(self, value: Any):
        if self.is_full():
            raise FixedStack.Full
        self.pointer += 1
        self.stack[self.pointer] = value

    def pop(self):
        if self.is_empty():
            raise FixedStack.Empty
        self.pointer -= 1
        return self.stack[self.pointer]

    def is_full(self) -> bool:
        if self.pointer >= self.capacity:
            return True
        return False

    def is_empty(self) -> bool:
        if self.pointer <= 0:
            return True
        return False
    
    def find(self, value: Any):
        for pointer in range(pointer, -1, -1): # 꼭대기 부터 선형검색
            if self.stack[pointer] == value:
                return pointer
            return -1
        
    def count(self, value:Any):
        count = 0
        for pointer in range(pointer, -1, -1):
            if self.stack[pointer] == value :
                count += 1
        
        return count
    
    def __contain__(self, value: Any):
        return self.count(value) > 0
    
    def dump(self):
        if self.is_empty():
            print(f'현재 스택이 비어있습니다.')
        else:
            print(self.stack[:self.pointer])