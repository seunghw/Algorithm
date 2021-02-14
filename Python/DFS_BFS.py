# 그래프 탐색 알고리즘 : DFS/BFS

# 탐색이란 많은 양의 데이터 중에서 원하는 데이터를  찾는 과정
# DFS/BFS는 코테에서 매우 자주 등장하는 유형!!!



# 미리 알아야하는 자료구조

# 1. 스택 자료구조

# 선입후출식 
# 입구와 출구가 동일한 형태

# _________________  <=
#|_________________  >=

stack = [] # 스택은 리스트 자료형을 쓰면 된다

stack.append(9)
stack.append(3)
stack.append(4)
stack.append(6)
stack.append(7)
stack.pop()
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력


# 2. 큐 자료구조

# 선입선출
# 입구출구 뚫려 있는 터널

#   _________________
#<= _________________ <=

from collections import deque

queue = deque()

queue.append(5)
queue.append(4)
queue.append(6)
queue.append(1)
queue.popleft()
queue.append(2)
queue.append(3)
queue.popleft()

print(queue) # 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력

# 큐를 구현할때는 리스트말고 덱을 해야 시간복잡도가 내려감
# (웬만하면 큐써라.)


# 재귀함수
# 자기 자신을 다시 호출하는 함수
# 단순한 형태의 재귀함수
'''
def recursive_function():
    print('재귀함수를 호출합니다.')
    recursive_function()

recursive_function()

'''
# 재귀 함수를 문제 풀이에서 사용할 때느 ㄴ재귀 함수의 종료 조건을 반드시 명시해야 합니다.
# 종료 조건을 제대로 명시하지 않으면 무한호출될 수 있음
# 종료 조건을 포함한 재귀 함수 예제
'''
def recursive_function(i):
    # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
    recursive_function(i +1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)
'''

# 팩토리얼 구현 예제
# n! = 1 * 2 * 3 * 4 * ... *(n-1) * n
# 수학적으로 0! 과 1!의 값은 1입니다.

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('반복적으로 구현:', factorial_recursive(5))

# 최대공약수 계산 (유클리드 호제법) 예제

# 두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘
# 두 자연수 a,b에 대하여 (a > b) a를 b로 나눈 나머지를 r이라고 하는데
# 이때 a와 b의 최대 공약수는 b와 r의 최대공약수와 같습니다.

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192,162))


# 모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현 가능
# 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많다


# DFS(Depth_FIrst Search)
# DFS는 깊이 우선 탐색이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘입니다.
# DFS는 스택 자료구조(혹은 재귀함수)를 이용합니다.
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리함
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 
# 그 노드를 스택에 넣고 방문처리, 방문하지 않은 인접 노드가 없으면 
# 스택에서 최상단 노드를 꺼냅니다
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복


# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적을 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 표현 (2차원 리스트)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)


# BFS (Breadth-First Search)
# BFS는 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘입니다.
# BFS는 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같습니다.
# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를
# 모두 큐에 삽입하고 방문처리
# 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 표현 ( 2차원 리스트 )
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)

# <문제> 음료수 얼려 먹기

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
'''
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<= -1 or x>= n or y<= -1 or y >=m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1

print(result) # 정답 출력

'''
# 미로 탈출
'''
# bfs 소스코드 구현
from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))

#def bfs(x,y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue 
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[nx][ny] + 1
                queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

'''