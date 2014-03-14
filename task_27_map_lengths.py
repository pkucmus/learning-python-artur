def map_lengths1(words):
    result = []
    for word in words:
        result.append(len(word))
    return result

def map_lengths2(words):
    return map(lambda word: len(word), words)

def map_lengths3(words):
    return [len(word) for word in words]

print map_lengths1(['ala','ma','kota']) == [3, 2, 4]
print map_lengths2(['ala','ma','kota']) == [3, 2, 4]
print map_lengths3(['ala','ma','kota']) == [3, 2, 4]
