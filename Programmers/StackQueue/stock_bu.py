from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
      price = prices.popleft()
      uptime = 0
      for next in prices:
        uptime += 1
        if price > next:
          break
      answer.append(uptime)

    return answer


print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]