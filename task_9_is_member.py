def is_member(x, a):
    for number in a:
        if x == number:
            return True

    return False;

print is_member(5, [1,2,3,4,5]) == True
print is_member(6, [1,2,3,4,5]) == False