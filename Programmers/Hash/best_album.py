from operator import itemgetter


def solution(genres, plays):

    play_count_dict = {}
    play_list_dict = {}

    for i in set(genres):
        play_count_dict[i] = 0
        play_list_dict[i] = []

    genre_play_tuple_list = list(zip(genres, plays))

    for index, (genre, play_count) in enumerate(genre_play_tuple_list):
        play_count_dict[genre] += play_count
        play_list_dict[genre].append((index, play_count))

    ret = []
    for i in sorted(play_count_dict.items(), key=lambda x: x[1], reverse=True):
        sorted_play_list = sorted(play_list_dict[i[0]], key=itemgetter(1), reverse=True)
        ret.extend(i[0] for i in sorted_play_list[:2])

    return ret


print(solution(['pop', 'pop', 'pop' ,'rap' ,'rap' ],
               [45, 50, 40, 60, 70]))
