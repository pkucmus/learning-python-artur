def reverse(string):
    result = ''

    for i in range(1, len(string) + 1):
        result += string[-i]

    return result

print reverse("I am testing") == "gnitset ma I"