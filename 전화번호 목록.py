def solution(phone_book):
    answer = True
    n=len(phone_book)
    for i in range(n):
        for j in range(i+1,n):
            a=0
            b=0
            
            for m in range(len(phone_book[i])):
                if len(phone_book[i][m])<=len(phone_book[j][m]):
                    if phone_book[i][m]==phone_book[j][m]:
                        a+=1
                        if a==(len(phone_book[i])):
                            answer=False
                            break
                else:
                    pass
                            
            for k in range(len(phone_book[j])):
                if len(phone_book[i][m])>=len(phone_book[j][m]):
                    if phone_book[i][m]==phone_book[j][m]:
                        b+=1
                        if b==(len(phone_book[j])):
                            answer=False
                            break
                    
            # 반대로 j가 i 보단 큰경우도 해야한다.
    return answer
  
  #이렇게 짰는데 런타임 오류랑 시간초과가뜬다 새로 효율적인 방법을 생각해야할듯..
  # 
