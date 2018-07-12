"""
This is lab 5
"""


def count_odd(x):
    """
    count odd
    """
    if isinstance(x, int):
        return 1 if x % 2 == 1 else 0
    return sum(count_odd(i) for i in x)


def count_longer_than(x, length):
    """
    count_longer_than
    """
    if isinstance(x, str):
        return 1 if len(x) > length else 0
    return sum(count_longer_than(i, length) for i in x)


def get_max_depth(x):
    """
    get max depth
    """
    if not isinstance(x, list):
        return 0
    return max([get_max_depth(i) for i in x]) + 1


def get_at_depth(x, depth):
    """
    get at depth
    """
    if not isinstance(x, list):
        if depth == 0:
            return [x]
        return []
    return sum([get_at_depth(item, depth - 1) for item in x], [])


if __name__ == '__main__':
    assert count_odd(1) == 1
    assert count_odd(2) == 0
    assert count_odd([1, 3, 4]) == 2
    assert count_odd([[1, 5, [[4, 6], 7]], 9]) == 4
    assert count_odd([1, [2, 3], [4, [5], [[6, 7], 8], 9]]) == 5

    assert count_longer_than('cat', 3) == 0
    assert count_longer_than('cat', 2) == 1
    assert count_longer_than(['', 'a', 'at', 'hat'], 1) == 2
    assert count_longer_than([['yes', 'no', [['ok', 'hat'], 'cat']], 'a'],
                             2) == 3
    assert count_longer_than(
        ['a', [['baby'], 'cat'], [['doll'], 'hat', [['cake'],
                                                    'hats']]], 3) == 4

    assert get_max_depth(5) == 0
    assert get_max_depth([1, 2, 3]) == 1
    assert get_max_depth([[1], 2]) == 2
    assert get_max_depth([1, [[3]], 8]) == 3
    assert get_max_depth([1, [2, [3]], [[[4]], 5]]) == 4

    assert get_at_depth(5, 0) == [5]
    assert get_at_depth(5, 1) == []
    assert get_at_depth([1, 2, 3], 1) == [1, 2, 3]
    assert get_at_depth([[1], 2, [3], 4], 1) == [2, 4]
    assert get_at_depth([1, [[3], 2, [4]], 8, [[5]]], 3) == [3, 4, 5]
    assert get_at_depth([1, [2, [3]], [[[4], 6], 5]], 3) == [3, 6]

    import python_ta

    python_ta.check_all(config="lab_pyta.txt")
