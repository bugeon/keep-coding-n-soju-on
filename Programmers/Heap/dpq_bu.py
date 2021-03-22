import heapq

def rearrange_heap(heap):
  result = []
  for n in heap:
    heapq.heappush(result, -n)
  return result

def solution(operations):
  answer = [0, 0]
  min_first = []
  max_first = []
  
  for op in operations:
    if op[0] == 'I':
      heapq.heappush(min_first, int(op.split()[1]))
      heapq.heappush(max_first, -int(op.split()[1]))
    else:
      try:
        if op.split()[1] == '1':
          heapq.heappop(max_first)
          min_first = rearrange_heap(max_first)
        else:
          heapq.heappop(min_first)
          max_first = rearrange_heap(min_first)
      except:
        continue

  if len(min_first) == 1:
    return [min_first[0], min_first[0]]
  elif len(min_first) == 0:
    return answer
  return [-max_first[0], min_first[0]]

operations = ["I 16","D 1"]	# [0,0]
print(solution(operations))
operations = ["I 7","I 5","I -5","D -1"]	# [7,5]  
print(solution(operations))