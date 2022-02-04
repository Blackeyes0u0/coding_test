
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    completion.append('zzzz')
    
    print(participant,completion)
    n=len(participant)
    for i in range(n):
        if participant[i]!=completion[i]:
            answer=participant[i]
            print(i)
            break #이걸 해주지않으면 다음 순서에서 또 바뀌어서 추가해준 항에서 틀리다고 해준다. 

    return answer
  
participant= ["mislav", "stanko", "mislav", "ana"]
completion=["stanko", "ana", "mislav"]
solution(participant,completion)

# hash함수를 이용해서 하는것.
# hash 함수란? https://ko.wikipedia.org/wiki/%ED%95%B4%EC%8B%9C_%ED%95%A8%EC%88%98


"""

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

해시 함수(hash function) 또는 해시 알고리즘(hash algorithm) 또는 해시함수알고리즘(hash函數algorithm)은 임의의 길이의 데이터를 고정된 길이의 데이터로 매핑하는 함수이다. 해시 함수에 의해 얻어지는 값은 해시 값, 해시 코드, 해시 체크섬 또는 간단하게 해시라고 한다. 그 용도 중 하나는 해시 테이블이라는 자료구조에 사용되며, 매우 빠른 데이터 검색을 위한 컴퓨터 소프트웨어에 널리 사용된다. 해시 함수는 큰 파일에서 중복되는 레코드를 찾을 수 있기 때문에 데이터베이스 검색이나 테이블 검색의 속도를 가속할 수 있다. 예를 들어서, DNA sequence에서 유사한 패턴을 찾는데 사용될 수도 있다. 또한 암호학에서도 사용될 수 있다. 암호용 해시 함수는 매핑된 해싱 값만을 알아가지고는 원래 입력 값을 알아내기 힘들다는 사실에 의해 사용될 수 있다. 또한 전송된 데이터의 무결성을 확인해주는 데 사용되기도 하는데, 메시지가 누구에게서 온 것인지 입증해주는 HMAC를 구성하는 블록으로 사용된다. 해시 함수는 결정론적으로 작동해야 하며, 따라서 두 해시 값이 다르다면 그 해시값에 대한 원래 데이터도 달라야 한다. (역은 성립하지 않는다) 해시 함수의 질은 입력 영역에서의 해시 충돌 확률로 결정되는데, 해시 충돌의 확률이 높을수록 서로 다른 데이터를 구별하기 어려워지고 검색하는 비용이 증가하게 된다.
해시함수중에는 암호학적 해시함수(Cryptographic Hash Function)와 비암호학적 해시함수로 구분되곤 한다.
암호학적 해시함수의 종류로는 MD5, SHA계열 해시함수가 있으며 비암호학적 해시함수로는 CRC32등이 있다.
암호학적 해시함수는 역상(pre-image), 제2역상(2nd pre-image), 충돌쌍(collision)에 대하여 안전성을 가져야 하며 인증에 이용된다 . 암호학적 해시함수는 임의의 길이를 입력 받기는 하지만 MD Strength Padding할 때 길이정보가 입력되므로 최대 길이에 대한 제한이 있다. 예를 들어 패딩시 하위 8비트에 길이정보가 입력 되는 경우에는 해시가능한 최대 길이는 0xFF가 되어 255바이트가 된다.(실제 길이정보는 패딩방식에 따라 다를 수 있다)


해시함수(hash函數)는 하나의 주어진 출력에 대하여 이 출력으로 사상시키는 하나의 입력을 찾는 것이 계산적으로 불가능하고, 하나의 주어진 입력에 대하여 같은 출력으로 사상시키는 또 다른 입력을 찾는 것이 계산적으로 불가능하다는 두 가지 성질을 만족하면서 임의의 비트열을 고정된 길이의 비트열로 사상시키는 함수이다.
"""
