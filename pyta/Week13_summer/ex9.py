"""
Fill in the dictionary RUNTIME_COMPLEXITIES, mapping the function with a given
name to one of the constants O_1, O_LGN, O_N, O_NLGN, O_N2, O_2N based on
the worst-case runtime complexity you think that function has.

O_1     = O(1) (constant time)
O_LGN   = O(lgn) (logarithmic time)
O_N     = O(n) (linear time)
O_NLGN  = O(nlgn) (nlgn time)
O_N2    = O(n^2) (quadratic time)
O_2N    = O(2^n) (exponential time)

For example, if you think the function apple() has quadratic runtime, you
should have
    "apple": O_N2
in RUNTIME_COMPLEXITIES.
"""
O_1 = "CONSTANT"
O_LGN = "LOGARITHMIC"
O_N = "LINEAR"
O_NLGN = "NLGN"
O_N2 = "QUADRATIC"
O_2N = "EXPONENTIAL"

RUNTIME_COMPLEXITIES = {"apple": O_N,
                        "banana": None,
                        "cat": None,
                        "dog": None,
                        "egg": None,
                        "flamingo": None,
                        "giraffe": None,
                        "helmet": None
                        }


def apple(n: int) -> None:
    """
    Mystery function 'apple'.

    Map "apple" in RUNTIME_COMPLEXITIES to the runtime of this function,
    with respect to n.
    """
    for i in range(n):
        for j in range(3):
            print("Apples!")


def banana(lst: list) -> None:
    """
    Mystery function 'banana'.

    Map "banana" in RUNTIME_COMPLEXITIES to the runtime of this function,
    with respect to the number of elements in lst.
    """
    new_list = lst
    something = lst[-1]
    while len(new_list) > 1:
        if something % 2 == 0:
            new_list = new_list[:len(new_list) // 2]
        else:
            new_list = new_list[len(new_list) // 2:]
        something = new_list[-1]


def cat(n: int) -> None:
    """
    Mystery function 'cat'.

    Map "cat" in RUNTIME_COMPLEXITIES to the runtime of this function,
    with respect to n.
    """
    for i in range(n):
        j = i
        while j > 1:
            j = j - 2


def dog(n: int) -> None:
    """
    Mystery function 'dog'.

    Map "dog" in RUNTIME_COMPLEXITIES to the runtime of this function,
    with respect to n.
    """
    something = []
    something_else = []
    i = 0
    while i < n:
        new = []
        something.append("A")
        something.append("S")
        for item in something:
            new.append(item)
        something_else.append(new)
        i = i + 1


def egg(n: int) -> None:
    """
    Mystery function 'egg'.

    Map "egg" in RUNTIME_COMPLEXITIES to the runtime of this function,
    with respect to n.
    """
    for i in range(n):
        j = i
        while j > 1:
            j = j // 2


def flamingo(lst: list) -> int:
    """
    Mystery function 'flamingo'.

    Map "flamingo" in RUNTIME_COMPLEXITIES to the runtime of this function,
    with respect to the number of elements in lst.
    """
    if lst == []:
        return 1

    if lst[-1] == 10:
        return 0

    return flamingo(lst[:-1])


def giraffe(n: int) -> str:
    """
    Mystery function 'giraffe'.

    Map "giraffe" in RUNTIME_COMPLEXITIES to the runtime of this function,
    with respect to n.
    """
    if n < 5:
        return "No"

    return giraffe(n // 2)


def helmet(lst: list) -> int:
    """
    Mystery function 'helmet'.

    Map "helmet" in RUNTIME_COMPLEXITIES to the runtime of this function,
    with respect to the number of elements in lst.
    """
    if len(lst) <= 1:
        return 1

    return helmet(lst[:len(lst) // 2]) + helmet(lst[len(lst) // 2:])