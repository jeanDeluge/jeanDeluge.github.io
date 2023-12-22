# KMP Knuth-Morris-Pratt 법

브루트 포스법은 일치하지 않는 문자를 만나면 다시 패턴의 첫문자부터 검사를 수행하지만, 검사했던 결과를 버리지 않고 문자열 검색을 하는 방법

# 방법

1. 텍스트 첫 문자가 맞지 않으면, 텍스트의 다음과 패턴 처음과 비교한다.
2. 텍스트와 패턴 안에서 겹치는 문자열을 찾아내서 검사를 다시 시작할 부분을 찾는다.
3. 건너뛰기 표를 만들어서 검사 결과를 그대로 사용할 수 있도록 한다.
    - 건너뛰기 표를 만든다면, 어디서 다시 시작할 수 있을지 확인할 수 있다.