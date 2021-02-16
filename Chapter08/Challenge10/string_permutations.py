from typing import Dict, List


def permutations(prefix: str, remain: str, cache: Dict[str, List[str]]):
    ret = set()

    if len(remain) == 0:
        ret.add(prefix)
        return ret

    if str in cache:
        for i in cache[remain]:
            ret.add(prefix+i)
        return ret

    for i in range(len(remain)):
        p = permutations(prefix + remain[i], remain[0:i] + remain[i + 1:len(remain)], cache)
        if len(remain[0:i] + remain[i + 1:len(remain)]) > 1:
            cache[remain[0:i] + remain[i + 1:len(remain)]] = [i[len(prefix)+1:] for i in p]
        ret = ret.union(p)

    return ret


def main():
    print(len(permutations('', 'ABCDE', dict())))

if __name__ == "__main__":
    main()
