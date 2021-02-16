from typing import List


def calculate_coins(remain: int, coins: List[int], index: int):
    count = 0

    if remain == 0:
        return 1

    if index == len(coins):
        return 0

    i = 0
    coin = coins[index]
    while i * coin <= remain:
        count += calculate_coins(remain - (i * coin), coins, index + 1)
        i += 1

    return count


def main():
    coins = [25, 10, 5, 1]

    print(calculate_coins(50, coins, 0))


if __name__ == "__main__":
    main()
