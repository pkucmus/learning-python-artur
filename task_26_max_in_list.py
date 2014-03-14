from task_1_max import max

def max_in_list(numbers):
    return reduce(lambda x, y: max(x, y), numbers)

print max_in_list([1,2,3,4,5,2,9,1,2,1,2,8,12,1]) == 12