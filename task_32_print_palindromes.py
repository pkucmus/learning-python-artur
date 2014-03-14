from task_17_is_palindrome import is_palindrome_ext

def print_palindromes(filename):
	file = open(filename, 'r')
	line = file.readline()
	while line != '':
		if is_palindrome_ext(line[:-1]):
			print line[:-1]
		line = file.readline()

	file.close()

print_palindromes("palindromy.in")