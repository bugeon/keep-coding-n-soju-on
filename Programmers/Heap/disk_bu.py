import heapq

def solution(jobs):
  total_time = 0
  count, last = 0, -1
  disk_queue = []
  jobs = sorted(jobs)
  time = jobs[0][0]
  
  while count < len(jobs):
    for request_time, duration in jobs:
      if last < request_time <= time:
        heapq.heappush(disk_queue, (duration, request_time))
    if len(disk_queue) > 0:
      count += 1
      last = time
      working_time, requst_time = heapq.heappop(disk_queue)
      time += working_time
      total_time += (time - requst_time)
    else:
        time += 1
  return total_time // count