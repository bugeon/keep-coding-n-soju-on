from typing import List


def step(n: int, cache: List[int] = None):

    if not cache:
        cache = [0] * (n+1)

    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif cache[n] > 0:
        return cache[n]

    cache[n] = step(n-1, cache) + step(n-2, cache) + step(n-3, cache)

    return cache[n]


def main():

    print(step(3))


if __name__ == "__main__":
    main()
