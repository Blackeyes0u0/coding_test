# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3

"""
def solution(n, lost, reserve):
    reserve = set(reserve)

    for size in [0,1,-2]:
        lost = set(map(lambda x : x+size, lost))
        reserve, lost = reserve-lost, lost- reserve
    
    return n-len(lost)
"""
def solution(n, lost, reserve):
    lost = set(lost)
    num_lost = len(lost)
    reserved = set(reserve) - set(lost)
    losted = set(lost) - set(reserve)

    for r in sorted(reserved):
        if r - 1 in losted:
            losted = losted - {r - 1}

        elif r + 1 in losted:
            losted = losted - {r + 1}
    return n-len(losted)
"""
def solution(n,lost,reserve):
    answer=0
    lost=set(lost)
    reserve=set(reserve)
    lost-=reserve
    reserve-=lost #중복 없애기
    
    for i in reserve:
        if i-1 in lost:
            lost-={i-1}
    for j in reserve:
        if j+1 in lost:
            lost=-{j+1}
            
    
    return n-len(lost)
"""
"""
def solution(n, lost, reserve):
    list1=[]
    list2=[]

    for i in range(len(lost)):
        for l in range(len(reserve)):
            if lost[i]==reserve[l]:
                #print(i)
                list1.append(i)
                list2.append(l)

    #print(list1,list2)
    list1.reverse()
    list2.reverse()
    
    for list in list1:
        lost.pop(list)
        
    for llii in list2:
        reserve.pop(llii)
    
    count=len(lost)
    
    for number in lost:
        for i in range(len(reserve)):
            s=reserve[i]
            reserve.remove(reserve[i])
            
            if number==s-1 or number==s+1:
                count-=1
                
                
                
    answer=n-count
    return answer

# 먼저 lost 와  reserve 에 중복되는값 찾아서 제거.

# if lost[0] 이 reserve 안에 있으면 제거.

# 총 lost  의 개수 찾기
"""
