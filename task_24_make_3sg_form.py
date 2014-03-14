def make_3sg_form(string):
    result = string
    if string.endswith('y'):
        result = string[:-2] + 'ies'
    elif string.endswith(('o', 'ch', 's', 'sh', 'x', 'z')):
        result += 'es'
    else:
        result += 's'
    return result

print make_3sg_form('try') == 'ties'
print make_3sg_form('brush') == 'brushes'
print make_3sg_form('run') == 'runs'
print make_3sg_form('fix') == 'fixes'
