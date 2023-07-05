from typing import Any

class FixedQueue:
    
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self) -> int:
        return self.no
    
    def is_empty(self) -> bool:
        return self.no <= 0
    
    def is_full(self) -> bool:
        return self.no >= self.capacity

    def enqueue(self, value: Any) -> None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = value
        self.rear += 1
        self.no += 1

        if self.rear == self.capacity:
            self.rear = 0

    def dequeue(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        value = self.que[self.front] 
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.fornt = 0
        return value
    
    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]
    
    def find(self, value : Any) -> Any:
        for i in range(self.no):
            ## 인덱스 위치는 front 에서 뒤로 가면서 확인해야하는데,
            ## 만약 front 가 capacity 값을 넘어간다면, 
            ## 0번째 인덱스부터 실행해야하는데, 이때는 나머지를 이용하면됨
            ## 만약 capacity = 10 (인덱스는 0 , 1, 2... 9) 이고
            ## front 현재 9 인데, i가 2 이면 인덱스는 1을 가르켜야한다. 
            ##  인덱스 1을 구하려면 9+2 / 10 ... 1

            idx = (self.front + i) % self.capacity
            if value == self.que[idx]:
                return idx
        
        return -1

    def count(self, value: Any) -> int:
        count = 0
        for i in range(self.no):
            idx =(i + self.front) % self.capacity
            if self.que[idx] == value:
                count += 1
        
        return count
    
    def __contain__(self, value: Any) -> bool:
        return self.find(value)
    
    def clear(self) -> None:
        self.no = self.front = self.rear = 0
        ## 굳이 원소를 삭제할 필요가 없다.
        ## 다 0으로 초기화해버린 후에 인큐하면 덮어씌워지기 때문

    def dump(self) -> None:
        if self.is_empty():
            print("큐에 데이터가 없음")
        else:
            for i in range(self.no):
                print(self.que[(i+self.fornt) % self.capacity], end="")
                ## [:rear]로 구현 안한 이유는 front 위치가 0 이 아닐 수 도 있기때문
                print()

