from typing import List, Tuple

size = 5


def is_valid(x, y):
    global size
    if x < 0 or y < 0 or x > (size - 1) or y > (size - 1):
        return False
    else:
        return True


def knight_tour(x, y, map: List[List[int]], moves: int, possible_coordinates: List[Tuple[int, int]]):
    global size
    if map[x][y] != 0:
        return
    else:
        map[x][y] = moves

    if moves == size * size:
        print(map)
        map[x][y] = 0
        return

    for i in possible_coordinates:
        if is_valid(x+i[0], y+i[1]):
            knight_tour(x+i[0], y+i[1], map, moves + 1, possible_coordinates)

    map[x][y] = 0


def main():
    possible_coordinates = [
        (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)
    ]

    knight_tour(0, 0, [[0 for i in range(size)] for j in range(size)],
                1, possible_coordinates)


if __name__ == "__main__":
    main()
