def sum(list):
    result = 0

    for number in list:
        result += number

    return result

def multiply(list):
    result = 1

    for number in list:
        result *= number

    return result

print sum([1,2,3,4]) == 10
print multiply([1,2,3,4]) == 24