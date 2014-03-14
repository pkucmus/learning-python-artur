def translate(string):
    vowels = ['a', 'e', 'i', 'o', 'u', ' ']
    result = ''

    for character in string:
        if character in vowels:
            result += character
        else:
            result += character + 'o' + character

    return result

print translate('this is fun') == 'tothohisos isos fofunon'