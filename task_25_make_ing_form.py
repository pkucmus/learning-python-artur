def make_ing_form(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''

    if string.endswith('ie'):
        result = string[:-2] + 'ying'
    elif string.endswith('e'):
        result = string[:-1] + 'ing'
    elif string[-3] not in vowels and string[-2] in vowels and string[-1] not in vowels:
        result = string+string[-1]+'ing'
    else:
        result = string + 'ing'

    return result

print make_ing_form('lie') == 'lying'
print make_ing_form('see') == 'seing'
print make_ing_form('move') == 'moving'
print make_ing_form('hug') == 'hugging'