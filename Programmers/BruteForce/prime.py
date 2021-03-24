from itertools import permutations


def generate_prime_list(n):
    sieve = [True] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i] == True]



def solution(numbers):
    numbers = sorted([c for c in numbers], reverse=True)
    max_number = int(''.join(numbers))

    prime_list = set(generate_prime_list(max_number))
    combined_numbers = set()

    for i in range(1, len(numbers) + 1):
        combined_numbers.update(list(map(int, map(''.join, permutations(numbers, i)))))

    return len(prime_list.intersection(combined_numbers))


print(solution("011"))

#
# def makeCombinations(str1, str2):
#     if str1 != "":
#         print(str1)
#
#     for i in range(len(str2)):
#         makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])
#
# makeCombinations("", "011")
#
#
#
# def solution(arr):
#     n = len(arr)
#     picked = []
#
#     def recur():
#         if len(picked) == 4:
#             print(picked)
#             return
#         for i in range(n):
#             if i not in picked:
#                 picked.append(i)
#                 recur()
#                 picked.pop()
#
#     recur()
#
# print(solution([0,1,2,3,4]))

