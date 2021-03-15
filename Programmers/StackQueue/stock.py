def solution(prices):
    answer = []
    for i in range(0, len(prices)):
        duration = 0
        while (duration + i + 1) < len(prices):
            duration += 1
            if prices[i] > prices[duration+i]:
                break
        answer.append(duration)

    return answer


print(solution([1, 2, 3, 2, 3]))