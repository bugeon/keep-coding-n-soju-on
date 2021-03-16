from operator import itemgetter


class Disk:
    def __init__(self, jobs):
        self.running_time = 0
        self.jobs = sorted(sorted(jobs, key=itemgetter(1)), key=itemgetter(0))
        self.waiting_time_list = []

    def run(self):
        if not self.jobs:
            return True
        else:
            if self.jobs[0][0] > self.running_time:
                self.running_time = self.jobs[0][0]
                return False
            else:

                job = self.jobs.pop(0)
                self.running_time += job[1]
                self.waiting_time_list.append(
                    self.running_time - job[0]
                )

                self.jobs = sorted(self.jobs, key=itemgetter(0))
                priority_jobs = list(filter(lambda x: x[0] <= self.running_time, self.jobs))
                priority_jobs = sorted(priority_jobs, key=lambda x: x[1])
                self.jobs = priority_jobs + self.jobs[len(priority_jobs):]


def solution(jobs):
    disk = Disk(jobs)
    while not disk.run():
        pass
    print(disk.waiting_time_list)
    return int(sum(disk.waiting_time_list) / len(disk.waiting_time_list))


print(solution([[0, 100], [0, 1]]))