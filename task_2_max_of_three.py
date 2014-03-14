from task_1_max import max

def max_of_three(x, y, z):
	return max(max(x, y), z)

print 9 == max_of_three(5, 3, 9)