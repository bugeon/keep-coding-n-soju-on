class DPQ:
    def __init__(self):
        self.list = []


    def add(self, item):
        self.list.append(item)
        self.list.sort()

    def del_max(self):
        if self.list:
            self.list.pop()

    def del_min(self):
        if self.list:
            self.list = self.list[1:]

def solution(operations):

    dpq = DPQ()

    for i in operations:
        operator, item = i.split(' ')
        if operator == 'I':
            dpq.add(int(item))
        elif operator == 'D':
            if int(item) == 1:
                dpq.del_max()
            elif int(item) == -1:
                dpq.del_min()

    if dpq.list:
        return [dpq.list[-1], dpq.list[0]]
    else:
        return [0, 0]


print(solution(["I 7","I 5","I -5","D -1"]))


import heapq
heap = [99, 3, 2, 1 , 111]
# heapq.heappush(heap, -1)
heapq.heapify(heap)
print(heap)

