import collections
from functools import reduce


def solution(clothes):
    clothes = collections.Counter([i for _, i in clothes])
    return reduce(lambda x, y: x * (y+1), clothes.values(), 1) - 1


print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))