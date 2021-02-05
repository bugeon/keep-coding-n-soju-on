from functools import lru_cache
from typing import List

array = [3, 2, 7, 4, 5, 1, 6, 7, 9]
visit: List[int] = []


@lru_cache(maxsize=None)
def subset_sum_cached(sum_of_subset, s, index):
    global visit
    global array

    if sum_of_subset > s:
        return

    if sum_of_subset == s:
        print([array[i] for i in visit])
        return

    for i in range(index, len(array)):
        visit.append(i)
        subset_sum_cached(sum_of_subset + array[i], s, i + 1)
        visit.pop()


def subset_sum(sum_of_subset, s, index, array, visit):
    if sum_of_subset > s:
        return

    if sum_of_subset == s:
        print([array[i] for i in visit])
        return

    for i in range(index, len(array)):
        visit.append(i)
        subset_sum(sum_of_subset + array[i], s, i + 1, array, visit)
        visit.pop()


def main():
    s = 7
    subset_sum(0, s, 0, array, list())
    # subset_sum_cached(0, s, 0)


if __name__ == "__main__":
    main()
