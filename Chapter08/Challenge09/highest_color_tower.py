from typing import List


class Box:
    def __init__(self, w: int, h: int, color: int):
        self.width = w
        self.height = h
        self.color = color

    def can_be_next(self, box):
        if box.width == -1:
            return True

        return ((box.width > self.width) and
                (box.height > self.height) and
                (box.color != self.color))


def get_height(box_list: List[Box], index: int, cache: List[int]):
    if cache[index] != 0:
        return cache[index]

    current_box = box_list[index]

    highest = 0

    for i in range(index+1, len(box_list)):
        if box_list[i].can_be_next(current_box):
            height = get_height(box_list, i, cache)
            if height > highest:
                highest = height

    highest = highest + current_box.height
    cache[index] = highest

    return highest


def prepare(box_list: List[Box]):
    box_list = sorted(box_list, key=lambda x: x.width, reverse=True)
    box_list.insert(0, Box(-1, 0, 0))
    return box_list


def main():

    box_list = [
        Box(2, 8, 1),
        Box(14, 10, 0),
        Box(10, 7, 1),
        Box(10, 5, 2),
        Box(10, 3, 1),
    ]

    box_list = prepare(box_list)

    print(get_height(box_list, 0, [0] * len(box_list)))


if __name__ == "__main__":
    main()
