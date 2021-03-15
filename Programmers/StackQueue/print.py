class Printer:

    def __init__(self, priorities):
        self.waiting_list = list(enumerate(priorities))
        self.highest = max(priorities)

    def print(self):
        index = 0
        while True:
            if self.waiting_list[index][1] == self.highest:
                location = self.waiting_list[index][0]
                self.waiting_list = self.waiting_list[index+1:] + self.waiting_list[:index]
                if self.waiting_list:
                    self.highest = max(map(lambda x: x[1], self.waiting_list))
                return location
            index += 1


def solution(priorities, location):
    run = 1
    p = Printer(priorities)
    while True:
        if p.print() == location:
            return run
        run += 1



print(solution([1]	, 0))