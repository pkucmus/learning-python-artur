def char_freq(string):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    result = {}

    for char in characters:
        NOchars = string.count(char)
        if NOchars:
            result[char] = string.count(char)

    return result

print char_freq('abbabcbdbabdbdbabababcbcbab') == {'a': 7, 'c': 3, 'b': 14, 'd': 3}