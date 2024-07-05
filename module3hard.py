data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    summ = 0
    for i in data_structure:
        if isinstance(i, list) == True or isinstance(i, tuple) == True or isinstance(i, set) == True:
            data_structure.remove(i)
            data_structure.extend(i)

        elif isinstance(i, dict) == True:
            data_structure.remove(i)
            data_structure.extend(list(zip(i.keys())))
            data_structure.extend(list(zip(i.values())))

        elif isinstance(i, list) == False or isinstance(i, tuple) == False or isinstance(i, dict) == False or isinstance(i, set) == False:
            pass

    for i in data_structure:
        if isinstance(i, list) == True or isinstance(i, tuple) == True or isinstance(i, dict) == True:
            calculate_structure_sum()

    for i in data_structure:
        if isinstance(i, int) == True:
            summ += i
        else:
            summ += len(i)

    return summ


result = calculate_structure_sum(data_structure)
print(result)

