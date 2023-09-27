def solution(s):
    answer = True
    P = 0
    Y = 0
    s = s.lower()
    for i in s:
        if i == 'p':
            P += 1
        elif i == 'y':
            Y += 1
    
    if P == Y:
        answer = True
    elif P == 0 and Y == 0:
        answer = True
    else:
        answer = False
    return answer