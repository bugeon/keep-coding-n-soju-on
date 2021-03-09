def clear_bits(n: int, k: int):
    return n & ((1 << k) - 1)


def main():
    print(clear_bits(7, 3))


if __name__ == "__main__":
    main()
