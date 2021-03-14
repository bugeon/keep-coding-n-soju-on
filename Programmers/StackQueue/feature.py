import math


def check_complete(progress_speeds, days):
    deploy_index = 0

    while progress_speeds and (progress_speeds[0][0] + days * progress_speeds[0][1] >= 100):
        deploy_index += 1
        progress_speeds.pop(0)

    return deploy_index


def solution(progresses, speeds):
    answer = []

    progress_speeds = list(zip(progresses, speeds))
    while progress_speeds:
        days = math.ceil((100 - progress_speeds[0][0])/progress_speeds[0][1])
        deploy = check_complete(progress_speeds, days)
        if deploy != 0:
            answer.append(deploy)

    return answer


print(solution(	[93, 30, 55],  [1, 30, 5]))
