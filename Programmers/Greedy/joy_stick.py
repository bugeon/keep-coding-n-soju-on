def convert_to_character_value_list(input):
    output = []
    for i in input:
        output.append(min(ord(i) - 65, 91 - ord(i)))
    return output


def minimum_count(cur_index, count, move_count_list):

    if count >= len(move_count_list):
        return count

    if sum(move_count_list) == 0:
        return min(count, len(move_count_list))

    next_index = (cur_index + 1) % len(move_count_list)
    previous_index = (cur_index - 1 + len(move_count_list)) % len(move_count_list)

    temp = move_count_list[next_index]
    move_count_list[next_index] = 0
    right = minimum_count(next_index, count + 1, move_count_list)
    move_count_list[next_index] = temp

    temp = move_count_list[previous_index]
    move_count_list[previous_index] = 0
    left = minimum_count(previous_index, count + 1, move_count_list)
    move_count_list[previous_index] = temp

    return min(right, left)


def solution(name):
    character_value_list = convert_to_character_value_list(name)

    character_value = sum(character_value_list)

    character_value_list[0] = 0
    minimum_moving_count = minimum_count(0, 0, character_value_list)

    return character_value + minimum_moving_count


print(solution("JAN"))