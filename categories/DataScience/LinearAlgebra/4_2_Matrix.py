from typing import Tuple, List

Matrix = List[List[float]]

## 열/ 행의 갯수 반환
def shape(A: Matrix) => Tuple[int, int]:
    num_rows = len(A) 
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

