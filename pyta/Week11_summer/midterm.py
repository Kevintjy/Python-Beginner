def get_element_counts(x) -> dict:
    """
    Return a dictionary containing the counts of each non-list item
    that appears in x.
    >>> get_element_counts('C')
    {'C': 1}
    >>> get_element_counts(['D', 'C', 'C'])
    {'D': 1, 'C': 2}
    >>> get_element_counts([10, [20, 'A'], [['B', 'A'], 20]])
    {10: 1, 20: 2, 'A': 2, 'B': 1}
    """
    if not isinstance(x, list):
        return {x : 1}
    else:
        result = {}
        for i in x:
            temp = get_element_counts(i)
            for j in temp:
                if j in result:
                    result[j] += 1
                else:
                    result[j] = 1
    return result