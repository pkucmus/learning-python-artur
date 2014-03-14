def generate_n_chars(n, c):
    #return n*c
    result = ''

    for i in range(n):
        result += c

    return result

print generate_n_chars(5, 'b') == 'bbbbb'