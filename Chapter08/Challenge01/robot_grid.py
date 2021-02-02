from typing import Set, List, Tuple


def compute_path(m: int, n: int, maze: List[List[bool]], path: List[Tuple], failed_path: Set[Tuple], memoization: bool):

    if not maze[m][n]:
        return False

    if m < 0 or n < 0:
        return False

    if memoization and (m, n) in failed_path:
        return False

    if m == 0 and n == 0:
        path.append((m, n))
        return True

    if compute_path(m - 1, n, maze, path, failed_path, memoization) or compute_path(m, n - 1, maze, path, failed_path, memoization):
        path.append((m, n))
        return True

    failed_path.add((m, n))
    return False


def main():
    maze = [[True, False, True, True],
            [True, False, True, True],
            [True, False, True, True],
            [True, True, True, True]]

    path = list()

    result = compute_path(3, 3, maze, path, set(), True)
    if result:
        for i in path:
            print(i)


if __name__ == "__main__":
    main()
