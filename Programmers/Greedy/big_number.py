def solution(number, k):
    answer = []
    while number != '':
        while k != 0 and answer and number[0] > answer[-1]:
            answer.pop()
            k -= 1

        answer.append(number[0])
        number = number[1:]

    while k != 0:
        answer.pop()
        k -= 1

    return ''.join(answer)


print(solution('999', 2))
