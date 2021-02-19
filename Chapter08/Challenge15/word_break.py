from typing import List, Set


# 2^n
def make_permutations(s: str, word_list: List[str], permutations: Set[str]):
    permutations.add(s)

    for i in range(len(word_list)):
        permutations = permutations.union(
            make_permutations(s + word_list[i], word_list[0:i] + word_list[i + 1:], permutations)
            )

    return permutations


def check_str(s: str, word_list: List[str]):
    permutations = make_permutations('', word_list, set())
    if s in permutations:
        return True
    else:
        return False


def check_str_memo(s: str, word_list: List[str]):

    memo = [False] * (len(s)+1)
    memo[0] = True
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if not memo[i]:
                break
            if s[i:j] in word_list:
                memo[j] = True

    return memo[len(s)]


def main():

    print(check_str_memo('thisisamazing', ['is', 'this', 'amazing']))


if __name__ == "__main__":
    main()
