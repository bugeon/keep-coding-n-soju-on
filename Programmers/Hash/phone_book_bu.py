def solution(phone_book):
    phone_book = sorted(phone_book)
    
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True

print(solution(["119", "97674223", "1195524421"])) # false
print(solution(["123","456","789"])) # true
print(solution(["12","123","1235","567","88"])) # false
