def find_odd(obj):
    if isinstance(obj, int):
        return [obj] if obj % 2 == 1 else []
    else:
        s = []
        for i in obj:
            s += find_odd(i)
        return s




print(find_odd([1,[2],3,[[[4,5,6],7],8],9]))