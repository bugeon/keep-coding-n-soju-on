from collections import Counter


def solution(citations):
    answer = 0

    citation_dict = dict.fromkeys(range(max(citations)), 0)
    citation_dict.update(Counter(citations))

    for k in reversed(range(max(citations)+1)):
        answer += citation_dict[k]
        if k <= answer:
            return k

    return 0


def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


print(solution([4, 4, 4, 0, 0, 0]))
