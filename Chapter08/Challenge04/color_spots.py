from typing import List, Set


def search_color_spots(i: int, j: int, row: int, col: int, color_map: List[List[int]], color: int, visit: Set[tuple]):
    if (i, j) in visit:
        return 0

    visit.add((i, j))

    if i < 0 or j < 0:
        visit.add((i, j))
        return 0

    if i > row or j > col:
        visit.add((i, j))
        return 0

    if color_map[i][j] == color:
        color_map[i][j] = -1
        return 1 + \
            search_color_spots(i+1, j, row, col, color_map, color, visit) + \
            search_color_spots(i-1, j, row, col, color_map, color, visit) + \
            search_color_spots(i, j+1, row, col, color_map, color, visit) + \
            search_color_spots(i, j-1, row, col, color_map, color, visit)

    return 0


def search_color_spots_with_queue(i: int, j: int, row: int, col: int, color_map: List[List[int]], color: int):
    queue = []
    ret = 0

    if color_map[i][j] == color:
        queue.append((i, j))

    while queue:
        i, j = queue.pop()

        if color_map[i][j] != -1:
            color_map[i][j] = -1
            ret += 1

        if i-1 >= 0 and color_map[i-1][j] == color:
            queue.append((i-1, j))
        if j-1 >= 0 and color_map[i][j-1] == color:
            queue.append((i, j-1))
        if i < row and color_map[i+1][j] == color:
            queue.append((i+1, j))
        if j < col and color_map[i][j+1] == color:
            queue.append((i, j+1))

    return ret


def search_biggest_color_spots(row: int, col: int, color_map: List[List[int]]):
    max_spots_size = 0
    for i in range(0, row):
        for j in range(0, col):
            if color_map[i][j] != -1:
                # spots_size = search_color_spots(i, j, row, col, color_map, color_map[i][j], set())
                spots_size = search_color_spots_with_queue(i, j, row, col, color_map, color_map[i][j])
                if spots_size > max_spots_size:
                    max_spots_size = spots_size
    return max_spots_size


def main():
    color_map = [[3, 2, 3, 1],
                 [1, 3, 1, 1],
                 [3, 2, 3, 1],
                 [3, 3, 3, 1]]

    print(search_biggest_color_spots(3, 3, color_map))


if __name__ == "__main__":
    main()
