def get_all_elements(x):
    if isinstance(x, int):
        return [x]
    return sum([get_all_elements(i) for i in x], [])


def passes_condition(f, x):
    if isinstance(x, int):
        if f(x):
            return [x]
        return []
    return sum([passes_condition(f,i) for i in x],[])


def count_number_of_lists(x):
    if isinstance(x, int):
        return 0
    return 1 + sum([count_number_of_lists(i) for i in x])


def all_sections_are_words(word, word_list):
    if len(word) <= 3:
        return word in word_list
    return all_sections_are_words(word[:len(word)//2],word_list) and\
           all_sections_are_words(word[len(word) // 2:],word_list) and\
           word in word_list


def get_nth_fibonacci(n):
    if n == 1: return 1
    if n == 2: return 1
    return get_nth_fibonacci(n-1) + get_nth_fibonacci(n-2)


def x_in_list(x, lst):
    if lst == []:
        return False
    if x == lst[0]:
        return True
    return x_in_list(x,lst[1:])


def x_in_sorted_list(x, lst):
    if len(lst) == 1:
        return x == lst[0]
    if x == lst[len(lst) // 2]:
        return True
    if x < lst[len(lst) // 2]:
        return x_in_sorted_list(x, lst[:len(lst) // 2])
    if x > lst[len(lst) // 2]:
        return x_in_sorted_list(x, lst[len(lst) //2:])


def binary_search(x, lst):
    if len(lst) == 1:
        return 0 if lst[0] == x else -1
    if lst == []:
        return -1
    mid_index = len(lst) // 2
    if x < lst[mid_index]:
        left = binary_search(x, lst[:mid_index])
        return left
    right = binary_search(x, lst[mid_index:])
    return mid_index + right if right > -1 else -1


def flatten_dictionary(d):
    new_dict = {}
    for k in d:
        if not isinstance(d[k], dict):
            new_dict[k] = d[k]
        else:
            recursive_dict = flatten_dictionary(d[k])
            for k1 in recursive_dict:
                add_key = k + '.' + k1
                new_dict[add_key] = recursive_dict[k1]
    return new_dict


def get_nth_fibonacci_memoized(n, fibonaccis = {}):
    fibonaccis[1] = 1
    fibonaccis[2] = 1
    if n in fibonaccis:
        return fibonaccis[n]
    value =  get_nth_fibonacci_memoized(n-2, fibonaccis) + get_nth_fibonacci_memoized(n-1, fibonaccis)
    fibonaccis[n] = value
    return value








if __name__ == '__main__':
    assert get_all_elements(5) == [5]
    assert get_all_elements([5, 15]) == [5, 15]
    assert get_all_elements([5, 15, [[25, 30], 45]]) == [5, 15, 25, 30, 45]
    assert get_all_elements([[5], 3, [1, [2], [3]]]) == [5, 3, 1, 2, 3]
    assert get_all_elements([[1, 2], [3, [4], [[5]]], [6, [7, [8, 9]], 10]]) == [1,
                                                                                 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def f(x):
        return x > 15
    assert passes_condition(f, 5) == []
    assert passes_condition(f, 25) == [25]
    assert passes_condition(f, [15, 25, 30]) == [25, 30]
    assert passes_condition(f, [[100, 3], [[15, 25, 30]], 45]) == [100, 25, 30, 45]
    assert passes_condition(f, [100, [[25, 3], 150, 10], [[30, [15, 20]], 5]]) == [100, 25, 150, 30, 20]

    assert count_number_of_lists(5) == 0
    assert count_number_of_lists([5]) == 1
    assert count_number_of_lists([[5], [3], [1]]) == 4
    assert count_number_of_lists([[5], 3, [1, [2], [3]]]) == 5

    assert all_sections_are_words("today", ['to', 'today']) == False
    assert all_sections_are_words("today", ['to', 'day', 'today']) == True
    assert all_sections_are_words("sometome", ['so', 'me', 'to']) == False
    assert all_sections_are_words("sometome", ['so', 'me', 'to', 'some']) == False
    assert all_sections_are_words("sometome", ['so', 'me', 'to', 'some', 'tome']) == False
    assert all_sections_are_words("sometome", ['so', 'me', 'to', 'some', 'tome',
                                               'sometome']) == True
    assert all_sections_are_words("sometome", ['so', 'me', 'some', 'tome',
                                               'sometome']) == False
    assert all_sections_are_words("sometome", ['so', 'me', 'to', 'tome',
                                               'sometome']) == False

    assert get_nth_fibonacci(1) == 1
    assert get_nth_fibonacci(2) == 1
    assert get_nth_fibonacci(3) == 2
    assert get_nth_fibonacci(10) == 55
    assert get_nth_fibonacci(15) == 610

    assert x_in_list(2, [-1, 0, 1]) == False
    assert x_in_list(1, [-5, 3, 1]) == True
    assert x_in_list(10, [1, -2, 10, -1, 15, 20]) == True
    assert x_in_list(15, [-1, 0, -4, 15, 3, 1]) == True
    assert x_in_list(20, [-1, 0, -4, 15, 3, 1]) == False

    assert x_in_sorted_list(2, [-1, 0, 1]) == False
    assert x_in_sorted_list(1, [-5, 0, 1]) == True
    assert x_in_sorted_list(10, [1, 10, 11, 15, 20]) == True
    assert x_in_sorted_list(15, [1, 2, 4, 10, 15, 18]) == True
    assert x_in_sorted_list(20, [1, 5, 7, 8, 10, 20]) == True
    assert x_in_sorted_list(25, [1, 5, 7, 8, 10, 20]) == False

    assert binary_search(2, [-1, 0, 1]) == -1
    assert binary_search(1, [-5, 0, 1]) == 2
    assert binary_search(10, [1, 10, 11, 15, 20]) == 1
    assert binary_search(15, [1, 2, 4, 10, 15, 18]) == 4
    assert binary_search(20, [1, 5, 7, 8, 10, 20]) == 5
    assert binary_search(25, [1, 5, 7, 8, 10, 20]) == -1

    d = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}}
    assert flatten_dictionary(d) == {'a': 1, 'b': 2, 'c.d': 3, 'c.e': 4}
    d = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4, 'f': {'g': 5}}}
    assert flatten_dictionary(d) == {'a': 1, 'b': 2, 'c.d': 3, 'c.e': 4, 'c.f.g': 5}

    assert get_nth_fibonacci_memoized(1) == 1
    assert get_nth_fibonacci_memoized(2) == 1
    assert get_nth_fibonacci_memoized(3) == 2
    assert get_nth_fibonacci_memoized(10) == 55
    assert get_nth_fibonacci_memoized(50) == 12586269025
    assert get_nth_fibonacci_memoized(100) == 354224848179261915075






