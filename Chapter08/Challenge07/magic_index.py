from typing import List


def find_magic(array: List[int], start, end):

    if start > end:
        return -1

    middle = int((start + end) / 2)

    left = find_magic(array, start, middle-1)
    if left != -1:
        return left

    if middle == array[middle]:
        return middle

    right = find_magic(array, middle+1, end)
    if right != -1:
        return right

    return -1


def main():
    ary = [1, 4, 4, 4, 5, 6, 5, 6, 6, 11, 12, 12, 12, 15, 17, 20, 21, 21]

    # 책에 있는 해답이 틀리는 케이스
    ary = [1, 4, 4, 4, 5, 5, 6, 6, 6, 11, 12, 12, 12]

    print(find_magic(ary, 0, len(ary) - 1))


if __name__ == "__main__":
    main()
