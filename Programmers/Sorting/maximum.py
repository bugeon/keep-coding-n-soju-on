from operator import itemgetter


def solution(numbers):
    number_value_list = [(i, str(i)*4) for i in numbers]
    number_value_list = sorted(number_value_list, key=itemgetter(1), reverse=True)
    if number_value_list[0][0] == 0:
        return '0'

    return ''.join([str(i[0]) for i in number_value_list])



numbers = [6, 10, 2]

print(solution([34, 3]))
