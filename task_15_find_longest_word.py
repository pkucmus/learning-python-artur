def find_longest_word(strings):
    result = 0

    for i in strings:
        result = max(len(i), result)

    return result

print find_longest_word(['ala','ma','kota']) == 4