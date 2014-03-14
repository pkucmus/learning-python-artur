def overlapping(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True

    return False

print overlapping([1,2,3,4,5],[6,7,8,9,10]) == False
print overlapping([1,2,3,4,5],[5,6,7,8,9,10]) == True