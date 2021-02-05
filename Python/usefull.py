

#자주 사용되는 내장함수

#sum()
result = sum([1, 2, 3, 4, 5])
print(result)

# min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result,max_result)

# eval()
result = eval("(3+5)*7")
print(result)


# sorted()
result = sorted([9, 1 ,8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)

# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)

# 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
# 순서를 고려해야함
# {'a','b','c'}에서 세개를 선택하여 나열: abc, acb, bac, bca, cab, cba

from itertools import permutations
data = ['A', 'B', 'C'] # 데이터 준비

result = list(permutations(data,3)) # 모든 수열 구하기
print(result)


# 조합 : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것.
# 순서 고려 안함
# {'a','b','c'}에서 두개를 선택하여 나열: ab, bc ,ca

from itertools import combinations
data = ['A', 'B', 'C'] # 데이터 준비

result = list(combinations(data,2)) # 모든 수열 구하기
print(result)


# 중복 순열과 중복 조합

from itertools import product

data = ['A', 'B', 'C'] # 데이터 준비

result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 ( 중복 허용 )
print(result)

from itertools import combinations_with_replacement

data = ['A', 'B', 'C'] # 데이터 준비

result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 ( 중복 허용 )


# Counter

# 등장 횟수를 세는 기능
# 리스트와 같은 반복 가능한(iterable) 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지를 알려줌

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue' ])

print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'이 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 반환 


# 최대 공약수와 최소 공배수

# 최대 공약수를 구해야 할 때는 math 라이브러리의 gcd() 함수를 이용할 수 있습니다.

import math

# 최소 공배수(LCM)를 구하는 함수
def lcm(a,b):
    return a * b // math.gcd(a,b)

a = 21
b = 14

print(math.gcd(21, 14)) # 최대 공약수(GCD) 계산
print(lcm(21, 14)) # 최소 공배수(LCM) 계산


# 시간 측정
'''
# 시간 측정
import time
start_time = time.time() # 측정 시작

# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력

'''