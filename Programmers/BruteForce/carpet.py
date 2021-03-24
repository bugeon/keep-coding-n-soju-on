import math


def solution(brown, yellow):

    for i in range(1, math.ceil(yellow ** 0.5)+1):
        if yellow % i == 0:
            v = i
            h = yellow // i

            if v * 2 + h * 2 + 4 == brown:
                return [h+2, v+2]

    return []

print(solution(24, 24))