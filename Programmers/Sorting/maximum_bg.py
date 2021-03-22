def solution(numbers):
  answer = ''
  numbers = [str(num) for num in numbers]
  numbers.sort(key = lambda x : x * 3, reverse = True)
  
  return str(int(''.join(numbers)))