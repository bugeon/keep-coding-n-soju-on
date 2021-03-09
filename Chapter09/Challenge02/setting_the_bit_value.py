def set_value(n: int, k: int, value: int):
    if value == 0:
        return n & ~ (1 << (k - 1))
    elif value == 1:
        return n | (value << (k - 1))

def main():
    print(set_value(4, 3, 0))


if __name__ == "__main__":
    main()
