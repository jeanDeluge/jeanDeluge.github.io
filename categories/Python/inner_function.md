abs(x) : 절대값
bool(x) :x 의 논리값 반환
complex(real, img) : 복소수 반환 또는 문자열 또는 수를 복소수로 변환한 값을 반환
divmod(a, b) : a를 b로 나누었을때의 몫과 나머지로 구성된 튜플 반환
float(x): 문자열 또는 수를 부동소수점 수로 변환하여 값을 반환
hex(x) : 정수값 x의 16진수
int(x, base): base:0~36 진수로 x를 반환
max(args1, arsg2, ..): 최댓값 반환
min(args1, arsg2, ..): 최솟값 반환
oct(x) : 8진수 반환
pow(x,y,z) : x의 y 제곱 반환, z를 입력시 x**y % z 를 반환. pow(x,y) % z 보다 효율적
round(n, ndigit) :n의 소수부를 ndigit 자리수가 되도록 반올림한 값
sum(x, start) : x의 원소값을 처음부터 끝까지 순서대로 더한 총합에 start를 더함. start 의 기본값은 0