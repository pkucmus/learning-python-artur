from task_1_max import max

def max_in_list(list):
    result = 0

    for i in list:
        result = max(i, result)

    return result

print max_in_list([1,2,3,4,5,6]) == 6