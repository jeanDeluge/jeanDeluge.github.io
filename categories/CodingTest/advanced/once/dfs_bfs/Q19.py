# 연산자 끼워넣기

# 2 : 주어진 숫자 개수
# 5 6 : 주어진 숫자
# 0 0 1 0 : 덧셈, 뺄셈, 곱하기 , 나누기 갯수

#출력
# 최대값
# 최소값

# 곱하기, 나누기가 연산자 우선순위 없음

input_1 = ["2", "5 6", "0 0 1 0"]
input_2  = ["3", "3 4 5", "1 0 1 0"]
def solution(numbers):
    n = int(numbers[0])
    numerals = list(map(int, numbers[1].split()))
    add, sub, mul, div = list(map(int, numbers[2].split()))
    
    stack = []

    def dfs(i, current):
        nonlocal add, sub, mul, div
        if i == n:
            stack.append(current)

        else:
            # 덧셈
            if add > 0:
                add -= 1
                dfs(i+1, current + numerals[i])
                add += 1

            if sub > 0:
                sub -= 1
                dfs(i+1,current -  numerals[i])
                sub += 1


            if mul > 0:
                mul -= 1
                dfs(i+1,current *  numerals[i])
                mul += 1


            if div > 0:
                div -= 1
                dfs(i+1,int(current /  numerals[i]))
                div += 1


    dfs(1, numerals[0])
    print(max(stack))
    print(min(stack))

solution(input_1)
solution(input_2)