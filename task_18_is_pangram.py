def is_pangram(string):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    for char in characters:
        if char not in string:
            return False

    return True

print is_pangram('The quick brown fox jumps over the lazy dog') == True