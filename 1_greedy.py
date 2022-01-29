#그리디 알고리즘

# 시간복잡도 

data= [1,1,3,5,6,2,22,1,1,1,3,4,2,4,3,3,4,5,16,6,3]

data.sort()
data

result=0
count=0
for i in data:
    count +=1
    #print(count)
    if count >=i:
        result +=1
        count=0
result

# 구현 implementation

# 풀이를 떠올리는 것은 쉽지만 소스코드로 옮긱기 어려운 문제를 지칭한다.


# 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 ㅂ벡터가 자주 활용된다.


##  상하좌우 문제 조건
#a = input()
#b = map(str,input().split())

# 문제는 요구사항대로 충실히 구현하면 된다.

#print(int(a),list(b))
b=["R","R","L","R","U","D","D","D"]
n=5
x=1
y=1
print(x,y)
def pp(i):
    global x
    global y
    if i=="R":
        if 1<=x<=n:
            x+=1
    elif i=="L":
        if 2<=x<=n:
            x-=1
    elif i=="U":
        if 2<=y<=n:
            y-=1
    elif i=="D":
        if 1<=y<=n:
            y+=1
    return x,y

for i in b:
    pp(i)

print(x,y)


#### 상하좌우 이동
plans=["R","R","L","R","U","D","D","D"]
n=5
x,y =1,1

move_types=['L','R','D',"U"]
dx=[-1,1,0,0]
dy=[0,0,+1,-1]

for plan in plans:
    for i in range(len(move_types)):
        if plan==move_types[i]:
            x+=dx[i]
            y+=dy[i]
print(x,y)


## 체스 나이트 이동

column=[1,2,3,4,5,6,8]
row=[1,2,3,4,5,6,7,8,]
#a1=A[i][j]

x,y=3,3

steps=[[-2,-1]]

data='d1'
data[0]

row = int(data[1])
column= int(ord(data[0]))-int(ord('a'))+1

print(row,column)

steps = [(-2,-1),(-1,-2),(1,-2)]

result=0
for step in steps:
    next = row+step[0]
    nextc = column+step[1]
    if next>=1 and next<=8 and nextc>=1 and nextc<=8:
        result+=1
print(result)


        

