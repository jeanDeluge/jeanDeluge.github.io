from typing import Tuple, List, Callable
Vector = List[float]
Matrix = List[List[float]]


## 열/ 행의 갯수 반환
def shape(A: Matrix) -> Tuple[int, int]:
    num_rows = len(A) 
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

# 열 가져오기

def get_rows(A: Matrix, i: int) -> Vector:
    return A[i]

# 행 가져오기
def get_columns(A: Matrix, j:int) -> Vector:
    return A_i[j] for A_i in A

# 단위행렬만들기
def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i, j: 1 if i==j else 0 )