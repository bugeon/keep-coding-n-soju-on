import math

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(total, 0, -1):
      if total % i == 0:
        # print(i)
        width = i
        height = total // i
        if (width - 2) * (height - 2) == yellow:
          return (width, height)
  
print(solution(50, 22))