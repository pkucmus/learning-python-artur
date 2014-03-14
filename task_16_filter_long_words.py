def filter_long_words(strings, n):
    result = []

    for string in strings:
        if len(string) > n:
            result.append(string)

    return result

print filter_long_words(['ala','ma','kota','asdffdf'], 3) == ['kota', 'asdffdf']