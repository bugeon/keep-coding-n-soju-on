def sum(p: int, q: int):
    _and = (p & q)
    xor = p ^ q

    while _and != 0:
        _and = _and << 1

        t = xor ^ _and
        _and = _and & xor

        xor = t

    return xor


print(sum(2, 2))