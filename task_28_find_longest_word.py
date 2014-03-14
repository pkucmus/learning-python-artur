def find_longest_word2(words):
    return reduce(lambda x, y: max(x, y), [len(word) for word in words])

print find_longest_word2(['ala','ma','kota']) == 4