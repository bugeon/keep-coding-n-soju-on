from typing import List

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def falling_ball(x: int, y: int, m: int, n: int, array: List[List[int]]):

    if array[x][y] == 0 :
        return

    current_high = array[x][y]
    array[x][y] = 0

    for i in direction:
        if x+i[0] < 0 or y+i[1] < 0 or x+i[0] == m or y+i[1] == n:
            continue
        if array[x+i[0]][y+i[1]] <= current_high:
            falling_ball(x + i[0], y + i[1], m, n, array)


def main():
    array = [[2, 1, 1, 2, 1],
           [3, 2, 2, 3, 2],
           [4, 1, 1, 3, 3],
           [4, 1, 1, 3, 4],
           [5, 4, 3, 4, 5]]

    falling_ball(4, 4, 5, 5, array)
    print(array)



if __name__ == "__main__":
    main()