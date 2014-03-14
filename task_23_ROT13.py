def ROT13_encode(string):
    result = ''

    for c in string:
        if c != ' ':
            if c.isupper():
                result += chr((ord(c)+13-65)%26+65)
            else:
                result += chr((ord(c)+13-97)%26+97)
        else:
            result += ' '

    return result

def ROT13_decode(string):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''

    for c in string:
        if c in characters:
            if c.isupper():
                result += chr((ord(c)-13-65)%26+65)
            else:
                result += chr((ord(c)-13-97)%26+97)
        else:
            result += c

    return result

print ROT13_encode('Caesar cipher? I much prefer Caesar salad!') == 'Pnrfne pvcuref V zhpu cersre Pnrfne fnynqb'
print ROT13_decode('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!') == 'Caesar cipher? I much prefer Caesar salad!'
