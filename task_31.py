def map(func, list):
    return [func(i) for i in list]

def filter(func, list):
    return [i for i in list if func(i)]

def reduce(func, list):
    result = list[0]
    for i, value in enumerate(list[:-1]):
        result = func(result, value)

    return result

print map(lambda word: len(word), ['aaa', 'b', 'ccccc', 'dd', 'eee']) == [3, 1, 5, 2, 3]
print filter(lambda word: len(word) > 4, ['aaa', 'b', 'ccccc', 'dd', 'eee']) == ['ccccc']
print reduce(lambda x, y: max(x, y), [len(word) for word in ['aaa', 'b', 'ccccc', 'dd', 'eee']]) == 5