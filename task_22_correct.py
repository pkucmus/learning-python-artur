def correct(string):
    import re
    def repl(match):
        return match.group(0)[0] + ' ' + match.group(0)[1]
    string = re.sub(r'[ ]{1,}', r' ', string)
    string = re.sub(r'([.][a-zA-z])', repl, string)

    return string

print correct('This   is  very funny  and    cool.Indeed! dsdads.dsadas') == 'This is very funny and cool. Indeed! dsdads. dsadas'