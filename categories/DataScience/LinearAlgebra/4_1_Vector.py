from typing import List

Vector = List[float]

height_weight_age = [70, 170, 40]
grade = [95, 80, 75, 62]

# 벡터의 덧셈의 의미 : 
# 같은 차원의 두 벡터에 대해서 
# 한 벡터의 꼬리부터 다른 벡터의 머리까지의 방향 => 물리에서는 방향과 크기가 다른 두 힘이 작용하는 방향

def add_vector(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]
    
# 벡터의 뺄셈의 의미
# 같은 차원의 두 벡터에 대해서, 두 백터가 가르키는 지점 사이의 거리나 차이를 나타냄

def substract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]


# 벡터의 내적
# 같은 차원의 두 벡터에 대해서, 두 벡터가 얼마나 비슷한 방향을 가지는 가 유사성을 나타내는 스칼라값

def dot(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be the same length"
    return sum([v_i * w_i in zip(v, w)])


# 벡터의 외적
# 삼차원 벡터로 만들어진 평면에 수직인 벡터를 생성한다. 물리에서는 두 벡터의 힘의 작요으로 회전하여 나아가는 힘의 방향 (나사)

def cross_product(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be the same length"
    
    result = [0, 0, 0]
    result[0] = v[1]*w[2] - v[2]*w[1]
    result[1] = v[2]*w[0] - v[0]*w[2]
    result[2] = v[0]*w[1] - v[1]*w[0]
    
    return result

## 각 성분의 제곱값의 합
def sum_of_squares(v: Vector) -> float:
    return dot(v, v)

## 벡터의 크기
def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))

## 벡터간의 거리
def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(substract(v, w))

##