# 15596번

def solved(a):
    return sum(a)

# 4673번
'''
delete_data = set() # 삭제할 set
numbers = set(range(1,10000)) 

for i in numbers:
    for n in str(i): 
        i += int(n)
    delete_data.add(i)

self_num = numbers - delete_data
for i in sorted(self_num):
   # print(i)
'''


# 1065 한수

n = int(input())
result=0

for i in range(1,n+1):
    if i < 100: # 1부터 99까지는 등차수열
        result += 1
    else:
     data = list(map(int,str(i))) # 숫자를 문자열로 바꿔서 분해
     if data[0] - data[1] == data[1] - data[2]: # 등차수열인지 판단
         result += 1

print(result)
