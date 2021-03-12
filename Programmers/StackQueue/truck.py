class Truck:
    def __init__(self, weight):
        self.weight = weight
        self.position = 0


class Queue:
    def __init__(self, length, weight):
        self.length = length
        self.max_weight = weight
        self.running_time = 0
        self.trucks = []

    def is_possible_to_enqueue(self, weight):
        return (sum(map(lambda x: x.weight, self.trucks)) + weight) <= self.max_weight

    def enqueue(self, truck: Truck):
        self.running_time += 1
        self.trucks.append(truck)
        for i in self.trucks:
            i.position += 1

        if self.trucks[0].position == self.length:
            self.trucks = self.trucks[1:]

    def run(self):
        if not self.trucks:
            if self.running_time == 0:
                return False
            self.running_time += 1
            return True
        else:
            time = self.length - self.trucks[0].position
            for i in self.trucks:
                i.position += time
            self.running_time += time
            self.trucks = self.trucks[1:]
            return False


def solution(bridge_length, weight, truck_weights):
    bridge: Queue = Queue(bridge_length, weight)
    truck_position = 0

    while not bridge.run():
        while (truck_position < len(truck_weights) and
               bridge.is_possible_to_enqueue(truck_weights[truck_position])):
            bridge.enqueue(Truck(truck_weights[truck_position]))
            truck_position += 1

    return bridge.running_time


print(solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]))
