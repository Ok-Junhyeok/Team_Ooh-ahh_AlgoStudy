# 단순 for, if 문
# def solution(arr):
#     answer = []
#     same_determine = arr[0]
#     answer.append(arr[0])
#     for i in range(1, len(arr)):
#         if arr[i] != same_determine:
#             answer.append(arr[i])
#         same_determine = arr[i]
#     return answer

def solution(arr):
    answer = []
    judge = arr[len(arr)-1] # 초기값 지정 -> LIFO 이므로 리스트 마지막 값

    for i in range(len(arr)-1, 0, -1):
        last = arr[i-1] # last에 [-2]값을 지정
        if judge == last: # 마지막 값과 그 앞의 값을 비교
            del arr[i-1]
        else:
            judge = last # 두 값이 서로 다르니까 판단하는 값 바꾸기
            
    answer = arr
    return answer
arr1 = [1,1,3,3,0,1,1]
arr2 = [4,4,4,3,3]

print(solution(arr1))
print(solution(arr2))