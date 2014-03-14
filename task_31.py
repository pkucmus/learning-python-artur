def map(func, list):
	result = []
	for i in list:
		result.append(func(i))

	return result

def filter(func, list):
	result = []
	for i in list:
		if func(i):
			result.append(i)

	return result

def reduce(func, list):
	result = list
	for i in range(len(list)-1):
		result[i+1] = func(result[i], list[i+1])

	return result[len(list)-2]

print map(lambda word: len(word), ['aaa', 'b', 'ccccc', 'dd', 'eee']) == [3, 1, 5, 2, 3]
print filter(lambda word: len(word) > 4, ['aaa', 'b', 'ccccc', 'dd', 'eee']) == ['ccccc']
print reduce(lambda x, y: max(x, y), [len(word) for word in ['aaa', 'b', 'ccccc', 'dd', 'eee']]) == 5