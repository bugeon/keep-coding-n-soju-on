def solution(genres, plays):
    answer = []
    genres_info = {}
    
    for i in range(len(genres)):
      if not genres[i] in genres_info:
        genres_info[genres[i]] = plays[i]
      else:
        genres_info[genres[i]] += plays[i]
        
    sorted_genres = sorted(genres_info.items(), key = lambda x: x[1], reverse = True)

    for i in range(len(sorted_genres)):
      first, second = 0, 0
      first_album_index, second_album_index = -1, -1
      for j in range(len(plays)):
        if sorted_genres[i][0] == genres[j]:
          if plays[j] > first:
            second, second_album_index = first, first_album_index
            first, first_album_index = plays[j], j
          elif plays[j] > second:
            second, second_album_index = plays[j], j
      if first_album_index != -1:
        answer.append(first_album_index)
      if second_album_index != -1:
        answer.append(second_album_index)
    return answer
  

genres, plays = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
print(solution(genres, plays)) #	[4, 1, 3, 0]
