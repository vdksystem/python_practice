def most_common_error(limit=5):
    errors = {}
    with open('resources/errors.txt') as err_file:
        for line in err_file:
            items = line.split()
            normalized = [item.lower() for item in items]
            for error in normalized:
                errors[error] = 1 if error not in errors else errors[error] + 1
    sorted_errors = sorted(errors, key=errors.get, reverse=True)
    result = {}
    for i, tor_error in zip(range(limit), sorted_errors):
        result[tor_error] = errors[tor_error]
    return result


print(most_common_error())
