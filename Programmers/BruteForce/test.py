import math


def generate_answer(n, count):
    if n == 1:
        return ([1, 2, 3, 4, 5] * math.ceil(count / 5))[:count-1]
    elif n == 2:
        return ([2, 1, 2, 3, 2, 4, 2, 5] * math.ceil(count / 8))[:count-1]
    elif n == 3:
        return ([3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * math.ceil(count / 10))[:count-1]

def solution(answers):
    answer = []
    for i in range(1, 4):
        candidates_answer = generate_answer(i, len(answers) + 1)
        for j in range(len(answers)):
            candidates_answer[j] = not(candidates_answer[j] ^ answers[j])
        answer.append(sum(candidates_answer))

    max_score = max(answer)
    answer = enumerate(answer, start=1)
    return list(map(lambda x : x[0], filter(lambda x: x[1] == max_score, answer)))


print(solution([1,2,3,4,5]))


