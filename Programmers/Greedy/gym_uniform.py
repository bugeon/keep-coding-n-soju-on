from typing import List


def solution(n, lost: List[int], reserve: List[int]):
    pure_reserve = set(reserve) - set(lost)
    pure_lost = set(lost) - set(reserve)

    borrow = 0
    for i in pure_lost:
        if i - 1 in pure_reserve:
            borrow += 1
            pure_reserve.remove(i-1)
        elif i + 1 in pure_reserve:
            borrow += 1
            pure_reserve.remove(i+1)

    return n - len(pure_lost) + borrow


print(solution(5, [2, 4], [3]))