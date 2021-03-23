def solution(citations):
  citations = sorted(citations)
  
  size = len(citations)
  for i in range( size):
    if citations[i] >= size - i:
      return i
  return 0

citations= [3, 0, 6, 1, 5]
print(solution(citations))
citations = [1]
print(solution(citations))
citations = [0, 2]
print(solution(citations))
citations= [0, 1, 4, 7 ,8 ,9]
print(solution(citations))