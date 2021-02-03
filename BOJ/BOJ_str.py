# 11654 아스키코드
'''
n = input()
print(ord(n))
'''

# 11720 숫자의 합
'''
n = int(input())
data = list(map(int,input()))

print(sum(data))
'''
# 10809 알파벳 찾기

'''
# 문자열 >> 아스키 == ord()
# 아스키 >> 문자열 == chr()
data = input()

result = list(range(97,123)) # 아스키코드 숫자범위

for i in result:
    print(data.find(chr(i)), end=' ')


'''
'''
# 2675 문자열 반복


t = int(input())

for i in range(t):
    r,s = input().split()
    text = ''
    for j in s:
        text += int(r) * j
    print(text)
'''
# 1157 단어 공부
'''
n = input().upper() # 전부 대문자로
data = [] # 가장 많이 사용된거 체크할 []
word_list = list(set(n)) # set으로 중복을 없애기

for i in word_list: 
    count = n.count(i) # 문자가 몇개 있었는지 카운트
    data.append(count) # 리스트에 추가

if data.count(max(data)) >= 2: # 가장 많이 쓴게 두개 이상이면
    print("?") # ? 출력
else:
    print(word_list[n.index(max(n))])


'''

# 1152 단어의 개수
'''
from collections import Counter

N = Counter(input())

print(N[' ']+1)
d
'''
'''
N = input().split()
print(len(N))

'''

# 2908번  상수
'''
a,b = input().split()

a = int(a[::-1])
b = int(b[::-1])

if a > b:
    print(a)
else: 
    print(b)
'''

# 5622번 다이얼
# 이 문제는 정리 한 번 더 해야할듯하다
words = input().lower()
s = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

time = 0
for i in range(len(words)):
    for j in s:
        if(words[i] in j):
            time += s.index(j) + 3
print(time)


