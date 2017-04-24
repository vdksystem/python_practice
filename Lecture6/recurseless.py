in_array = [1, [2, 3], 4, [5, [6, 7], [8, 9]]]


def recurseless(arr):
    iterator = arr
    while True:
        result = []
        for i in iterator:
            if isinstance(i, list):
                result.extend(i)
            else:
                result.append(i)
        iterator = result
        break_cond = True
        for item in iterator:
            if isinstance(item, list):
                break_cond = False
        if break_cond:
            break
    return result


print(recurseless(in_array))


