#n=input()
x=3
#x=[]
if (x%10)==3:
    pass

a = [i  for i in range(0,24)]
b = [i for i in range(0,60)]
c = [i for i in range(0,60)]

# h= input()
count=0
h=24
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1
count


# chess night move count

#input_data= input()
input_data='c2'
row =int(input_data[1])
column=int(ord(input_data[0])-ord('a'))+1
steps =[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result=0
for step in steps:

    next_row= row+step[0]
    next_column=column+step[1]
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        result+=1
print(result)





# game development
# map_dim(nxm) direction setting, start point , map
#n,m = input().split()
n,m=map(int,input().split())
d= [[0]*m for _ in range(n)]
#d= [[0 for j in range(m)] for i in range(n)]
d =[[0]*m for _ in range(n)]

x,y,direction = map(int,input().split())
d[x][y]=1 #현재 좌표 방문처리
# 맵전체 정보

array=[]
for i in range(n):
    array.append(list(map,input().split()))

#   북 동 남서
dx=[-1,0,1, 0]
dy=[0, 1,0,-1]

def turn_left():
    global direction
    direction==1
    if direction==-1:
        direction=3
# start simulation
count=1
turn_time=0
while True:
    turn_left()
    nx=x+
