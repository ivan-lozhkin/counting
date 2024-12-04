data_structure = [

[1, 2, 3],

{'a': 4, 'b': 5},

(6, {'cube': 7, 'drum': 8}),

"Hello",

((), [{(2, 'Urban', ('Urban2', 35))}])

]

def calculate_structure_sum(data, *args):
    total = 0
    if isinstance(data, (int, float)):
        total += data
    elif isinstance(data, str):
        total += len(data)
    elif isinstance(data, (list, set, tuple)):
        for item in data:
            total += calculate_structure_sum(item, *args)
    elif isinstance(data, dict):
        for v, k in data.items():
            total += calculate_structure_sum(v, *args)
            total += calculate_structure_sum(k, *args)
    # elif isinstance(data, tuple):
    #     for elem in data:
    #         total += calculate_structure_sum(elem, *args)
    return total + sum(args)

result = calculate_structure_sum(data_structure)
print(result)

