def get_value(n: int, k: int):
    return 1 & (n >> (k - 1))


def main():
    print(get_value(4, 2))


if __name__ == "__main__":
    main()
