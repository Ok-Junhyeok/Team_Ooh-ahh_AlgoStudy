import sys
input = sys.stdin.readline # 이거 안 쓰면 시간초과 자주 나옴(백준)

N = int(input())
arr = []

for i in range(N):
  NUA = int(input())
  arr.append(NUA)

def ppoopp(array):
  if len(array) != 0:
    return array.pop(-1) # 배열의 마지막 값 리턴 후, 그 배열에서 삭제 처리

larger = ppoopp(arr) # 리스트의 마지막 값(초기 설정)
flag = 1 # 보이는 막대기 수(초기 설정)

for i in range(len(arr), 0, -1):
  box = ppoopp(arr)
  if box > larger:
    larger = box
    flag += 1

print(flag)