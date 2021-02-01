# grid(탐욕법) 현재 상황에서 지금 당장 좋은 것만 고르는 방법.
# 일반적인 그리디 알고리즘은 문제를  풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구
# 그리디 해법은 그 정당성 분석이 중요!!
# 최적의 해를 구할 수 있는지.
# 일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없을 때가 많다.
# 하지만 코테에서 대부분의 그리디 문제는 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론할 수 있어야 풀리도록 출제

# 거스름돈 문제
'''
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)


# 1이 될 때까지

# n, k를 공백을 기준으로 구분하여 입력 받기
n,k = map(int,input().split())

count = 0

while n != 1: 
    if n % k == 0:
        n = n / k
        count += 1
       
    else:
        n = n-1
        count += 1

# 시간복잡도를 생각하면 아래가 좋음

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n-target)
    n = target
    # N이 K보다 작을 대 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

result += (n-1)
print(result)

print(count)



# 곱하기 혹은 더하기

data = input()

result = int(data[0])

for i in range(1,len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)


# 모험가 길드


n = int(input())

data = list(map(int,input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력


# 시뮬레이션과 완전탐색

# 구현 유형의 예시
# 알고리즘은 간단하지만 코드가 지나칠 만큼 길어지는 문제
# 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
# 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
# 적절한 라이브러리를 찾아서 사용해야 하는 문제

# 일반적으로 2차원 공간 즉, 행렬을 많이 사용함

# 2차원 행렬

for i in range(5):
    for j in range(5):
        print('(', i, ',', j, ')', end=' ')
    print()


# 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용됨

# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x, y = 2, 2

for i in range(4):
    # 다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)
    



# 상하좌우

n = int(input())
x, y = 1, 1

plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx> n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)



# 시각
# 이 문제는 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제
# 이러한 유형은 완전탐색(Brute Forcing)이라고 한다.

h = int(intput())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)


# 왕실의 나이트

# 현재 나이트의 위치 입력받기

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1),(-1, -2),(1, -2),(2, -1),(2, 1),(1, 2),(-1, 2),(-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
        result += 1

print(result)

'''
# 문자열 재정렬

n = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in n:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더함
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result)) 