def solution(phone_book):
    phone_book = sorted(phone_book,key=len, reverse=True)
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for number in phone_book:
        for i in range(1, len(number)) :
            if number[:i] in hash_map and number[:i] != number :
                return False
    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))